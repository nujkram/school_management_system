"""
School Management System
Description for School Management System

Author: Empty (empty@gmail.com)
Version: 0.0.1
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from academic_years.models import AcademicYearSubject
from accounts.mixins.user_type_mixins import IsFacultyViewMixin
from accounts.models import Account
from accounts.models.account.constants import STUDENT

from subjects.models.subject_student.models import SubjectStudent as Master
from faculty_dashboard.controllers.views.faculty_dashboard.subject_students.forms import SubjectStudentForm as MasterForm

"""
URLS
# Subject Student

from faculty_dashboard.controllers.views.faculty_dashboard.subject_students import main as subject_students_views

urlpatterns += [
    path(
        'subject_student/list',
        subject_students_views.FacultyDashboardSubjectStudentListView.as_view(),
        name='faculty_dashboard_subject_students_list'
    ),
    path(
        'subject_student/<subject_student>/detail',
        subject_students_views.FacultyDashboardSubjectStudentDetailView.as_view(),
        name='faculty_dashboard_subject_students_detail'
    ),
    path(
        'subject_student/create',
        subject_students_views.FacultyDashboardSubjectStudentCreateView.as_view(),
        name='faculty_dashboard_subject_students_create'
    ),
    path(
        'subject_student/<subject_student>/update',
        subject_students_views.FacultyDashboardSubjectStudentUpdateView.as_view(),
        name='faculty_dashboard_subject_students_update'
    ),
    path(
        'subject_student/<subject_student>/delete',
        subject_students_views.FacultyDashboardSubjectStudentDeleteView.as_view(),
        name='faculty_dashboard_subject_students_delete'
    )
]
"""


class FacultyDashboardSubjectStudentListView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    List view for Subject Students. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Faculty user

    Filters:
        - Optionally used more multi-user/multi-tenant apps to separate ownership
        - ex: company=kwargs.get('company')
    """

    def get(self, request, *args, **kwargs):
        obj_list = Master.objects.actives()
        paginator = Paginator(obj_list, 50)
        page = request.GET.get('page')
        objs = paginator.get_page(page)

        context = {
            "page_title": f"Subject Students",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "subject_student",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "faculty_dashboard/subject_students/list.html", context)


class FacultyDashboardSubjectStudentCreateView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Subject Students. 
    
    Allowed HTTP verbs: 
        - GET
        - POST
    
    Restrictions:
        - LoginRequired
        - Faculty user

    Filters:
        - Optionally used more multi-user/multi-tenant apps to separate ownership
        - ex: company=kwargs.get('company')
    """

    def get(self, request, *args, **kwargs):
        academic_year_subject_pk = request.GET.get('academic_year_subject')
        form = MasterForm()
        if academic_year_subject_pk:
            academic_year_subject = AcademicYearSubject.objects.get(pk=academic_year_subject_pk)
            form = MasterForm(initial={'subject': academic_year_subject.subject})

        form.fields['student'].queryset = Account.objects.filter(user_type=STUDENT)

        context = {
            "page_title": "Create new Subject Student",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "subject_student",
            "menu_action": "create",
            "form": form
        }

        return render(request, "faculty_dashboard/subject_students/form.html", context)
    
    def post(self, request, *args, **kwargs):
        form = MasterForm(data=request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.created_by = request.user
            data.save()
            messages.success(
                request,
                f'{data} saved!',
                extra_tags='success'
            )

            return HttpResponseRedirect(
                reverse(
                    'faculty_dashboard_subjects_detail',
                    kwargs={
                        'subject_student': data.subject.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Subject Student",
                "menu_section": "faculty_dashboard",
                "menu_subsection": "subject_student",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "faculty_dashboard/subject_students/form.html", context)


class FacultyDashboardSubjectStudentDetailView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Subject Students. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Faculty user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('subject_student', None))
        context = {
            "page_title": f"Subject Student: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "subject_student",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "faculty_dashboard/subject_students/detail.html", context)


class FacultyDashboardSubjectStudentUpdateView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Subject Students. 
    
    Allowed HTTP verbs: 
        - GET
        - POST
    
    Restrictions:
        - LoginRequired
        - Faculty user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('subject_student', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Subject Student: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "subject_student",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "faculty_dashboard/subject_students/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('subject_student', None))
        form = MasterForm(instance=obj, data=request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.updated_by = request.user
            data = form.save()
            messages.success(
                request,
                f'{data} saved!',
                extra_tags='success'
            )

            return HttpResponseRedirect(
                reverse(
                    'faculty_dashboard_subject_students_detail',
                    kwargs={
                        'subject_student': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Subject Student: {obj}",
                "menu_section": "faculty_dashboard",
                "menu_subsection": "subject_student",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "faculty_dashboard/subject_students/form.html", context)


class FacultyDashboardSubjectStudentDeleteView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Subject Students. 
    
    Allowed HTTP verbs: 
        - GET
        - POST
    
    Restrictions:
        - LoginRequired
        - Faculty user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('subject_student', None))
        context = {
            "page_title": "Delete Subject Student: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "subject_student",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "faculty_dashboard/subject_students/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('subject_student', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'faculty_dashboard_subject_students_list'
            )
        )
