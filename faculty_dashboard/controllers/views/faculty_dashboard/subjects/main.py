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
from subjects.models import SubjectStudent

from subjects.models.subject.models import Subject as Master
from faculty_dashboard.controllers.views.faculty_dashboard.subjects.forms import SubjectForm as MasterForm

"""
URLS
# Subject

from faculty_dashboard.controllers.views.faculty_dashboard.subjects import main as subjects_views

urlpatterns += [
    path(
        'subject/list',
        subjects_views.FacultyDashboardSubjectListView.as_view(),
        name='faculty_dashboard_subjects_list'
    ),
    path(
        'subject/<subject>/detail',
        subjects_views.FacultyDashboardSubjectDetailView.as_view(),
        name='faculty_dashboard_subjects_detail'
    ),
    path(
        'subject/create',
        subjects_views.FacultyDashboardSubjectCreateView.as_view(),
        name='faculty_dashboard_subjects_create'
    ),
    path(
        'subject/<subject>/update',
        subjects_views.FacultyDashboardSubjectUpdateView.as_view(),
        name='faculty_dashboard_subjects_update'
    ),
    path(
        'subject/<subject>/delete',
        subjects_views.FacultyDashboardSubjectDeleteView.as_view(),
        name='faculty_dashboard_subjects_delete'
    )
]
"""


class FacultyDashboardSubjectListView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    List view for Subjects. 
    
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
            "page_title": f"Subjects",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "subject",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "faculty_dashboard/subjects/list.html", context)


class FacultyDashboardSubjectCreateView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Subjects. 
    
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
        form = MasterForm
        context = {
            "page_title": "Create new Subject",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "subject",
            "menu_action": "create",
            "form": form
        }

        return render(request, "faculty_dashboard/subjects/form.html", context)
    
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
                        'subject': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Subject",
                "menu_section": "faculty_dashboard",
                "menu_subsection": "subject",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "faculty_dashboard/subjects/form.html", context)


class FacultyDashboardSubjectDetailView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Subjects. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Faculty user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        academic_year_subject = AcademicYearSubject.objects.get(pk=kwargs.get('subject'))
        subject_students = SubjectStudent.objects.filter(subject=academic_year_subject.pk)
        obj = get_object_or_404(Master, pk=academic_year_subject.subject.pk)
        context = {
            "page_title": f"Subject: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "subject",
            "menu_action": "detail",
            "academic_year_subject": academic_year_subject,
            "subject_students": subject_students,
            "obj": obj
        }

        return render(request, "faculty_dashboard/subjects/detail.html", context)


class FacultyDashboardSubjectUpdateView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Subjects. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('subject', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Subject: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "subject",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "faculty_dashboard/subjects/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('subject', None))
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
                    'faculty_dashboard_subjects_detail',
                    kwargs={
                        'subject': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Subject: {obj}",
                "menu_section": "faculty_dashboard",
                "menu_subsection": "subject",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "faculty_dashboard/subjects/form.html", context)


class FacultyDashboardSubjectDeleteView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Subjects. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('subject', None))
        context = {
            "page_title": "Delete Subject: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "subject",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "faculty_dashboard/subjects/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('subject', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'faculty_dashboard_subjects_list'
            )
        )
