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

from academic_years.models import AcademicYear
from accounts.mixins.user_type_mixins import IsFacultyViewMixin

from academic_years.models.academic_year_subject.models import AcademicYearSubject as Master
from faculty_dashboard.controllers.views.faculty_dashboard.academic_year_subjects.forms import \
    AcademicYearSubjectForm as MasterForm

"""
URLS
# Academic Year Subject

from faculty_dashboard.controllers.views.faculty_dashboard.academic_year_subjects import main as academic_year_subjects_views

urlpatterns += [
    path(
        'academic_year_subject/list',
        academic_year_subjects_views.FacultyDashboardAcademicYearSubjectListView.as_view(),
        name='faculty_dashboard_academic_year_subjects_list'
    ),
    path(
        'academic_year_subject/<academic_year_subject>/detail',
        academic_year_subjects_views.FacultyDashboardAcademicYearSubjectDetailView.as_view(),
        name='faculty_dashboard_academic_year_subjects_detail'
    ),
    path(
        'academic_year_subject/create',
        academic_year_subjects_views.FacultyDashboardAcademicYearSubjectCreateView.as_view(),
        name='faculty_dashboard_academic_year_subjects_create'
    ),
    path(
        'academic_year_subject/<academic_year_subject>/update',
        academic_year_subjects_views.FacultyDashboardAcademicYearSubjectUpdateView.as_view(),
        name='faculty_dashboard_academic_year_subjects_update'
    ),
    path(
        'academic_year_subject/<academic_year_subject>/delete',
        academic_year_subjects_views.FacultyDashboardAcademicYearSubjectDeleteView.as_view(),
        name='faculty_dashboard_academic_year_subjects_delete'
    )
]
"""


class FacultyDashboardAcademicYearSubjectListView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    List view for Academic Year Subjects. 
    
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
        academic_year_pk = kwargs.get('academic_year')
        academic_year = AcademicYear.objects.get(pk=academic_year_pk)

        obj_list = Master.objects.filter(academic_year=academic_year, faculty=request.user).actives()

        paginator = Paginator(obj_list, 50)
        page = request.GET.get('page')
        objs = paginator.get_page(page)

        context = {
            "page_title": f"School Year Subjects",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "academic_year_subject",
            "menu_action": "list",
            "paginator": paginator,
            "academic_year": academic_year,
            "objects": objs
        }

        return render(request, "faculty_dashboard/academic_year_subjects/list.html", context)


class FacultyDashboardAcademicYearSubjectCreateView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Academic Year Subjects. 
    
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
            "page_title": "Create new School Year Subject",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "academic_year_subject",
            "menu_action": "create",
            "form": form
        }

        return render(request, "faculty_dashboard/academic_year_subjects/form.html", context)

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
                    'faculty_dashboard_academic_year_subjects_detail',
                    kwargs={
                        'academic_year_subject': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new School Year Subject",
                "menu_section": "faculty_dashboard",
                "menu_subsection": "academic_year_subject",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "faculty_dashboard/academic_year_subjects/form.html", context)


class FacultyDashboardAcademicYearSubjectDetailView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Academic Year Subjects. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Faculty user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('academic_year_subject', None))
        context = {
            "page_title": f"School Year Subject: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "academic_year_subject",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "faculty_dashboard/academic_year_subjects/detail.html", context)


class FacultyDashboardAcademicYearSubjectUpdateView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Academic Year Subjects. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('academic_year_subject', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update School Year Subject: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "academic_year_subject",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "faculty_dashboard/academic_year_subjects/form.html", context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('academic_year_subject', None))
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
                    'faculty_dashboard_academic_year_subjects_detail',
                    kwargs={
                        'academic_year_subject': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update School Year Subject: {obj}",
                "menu_section": "faculty_dashboard",
                "menu_subsection": "academic_year_subject",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "faculty_dashboard/academic_year_subjects/form.html", context)


class FacultyDashboardAcademicYearSubjectDeleteView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Academic Year Subjects. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('academic_year_subject', None))
        context = {
            "page_title": f"Delete School Year Subject: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "academic_year_subject",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "faculty_dashboard/academic_year_subjects/delete.html", context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('academic_year_subject', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'faculty_dashboard_academic_year_subjects_list'
            )
        )
