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

from accounts.mixins.user_type_mixins import IsAdminViewMixin

from academic_years.models.academic_year_subject.models import AcademicYearSubject as Master
from admin_dashboard.controllers.views.admin_dashboard.academic_year_subjects.forms import AcademicYearSubjectForm as MasterForm

"""
URLS
# Academic Year Subject

from admin_dashboard.controllers.views.admin_dashboard.academic_year_subjects import main as academic_year_subjects_views

urlpatterns += [
    path(
        'academic_year_subject/list',
        academic_year_subjects_views.AdminDashboardAcademicYearSubjectListView.as_view(),
        name='admin_dashboard_academic_year_subjects_list'
    ),
    path(
        'academic_year_subject/<academic_year_subject>/detail',
        academic_year_subjects_views.AdminDashboardAcademicYearSubjectDetailView.as_view(),
        name='admin_dashboard_academic_year_subjects_detail'
    ),
    path(
        'academic_year_subject/create',
        academic_year_subjects_views.AdminDashboardAcademicYearSubjectCreateView.as_view(),
        name='admin_dashboard_academic_year_subjects_create'
    ),
    path(
        'academic_year_subject/<academic_year_subject>/update',
        academic_year_subjects_views.AdminDashboardAcademicYearSubjectUpdateView.as_view(),
        name='admin_dashboard_academic_year_subjects_update'
    ),
    path(
        'academic_year_subject/<academic_year_subject>/delete',
        academic_year_subjects_views.AdminDashboardAcademicYearSubjectDeleteView.as_view(),
        name='admin_dashboard_academic_year_subjects_delete'
    )
]
"""


class AdminDashboardAcademicYearSubjectListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    List view for School Year Subjects.
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - Optionally used more multi-user/multi-tenant apps to separate ownership
        - ex: company=kwargs.get('company')
    """

    def get(self, request, *args, **kwargs):
        obj_list = Master.objects.filter(pk=kwargs.get('academic_year_subject'))
        obj = obj_list.first()
        paginator = Paginator(obj_list, 50)
        page = request.GET.get('page')
        objs = paginator.get_page(page)

        context = {
            "page_title": f"School Year Subjects",
            "menu_section": "admin_dashboard",
            "menu_subsection": "academic_year_subject",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs,
            "obj": obj
        }

        return render(request, "admin_dashboard/academic_year_subjects/list.html", context)


class AdminDashboardAcademicYearSubjectCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Academic Year Subjects. 
    
    Allowed HTTP verbs: 
        - GET
        - POST
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - Optionally used more multi-user/multi-tenant apps to separate ownership
        - ex: company=kwargs.get('company')
    """

    def get(self, request, *args, **kwargs):
        form = MasterForm()
        academic_year = request.GET.get('academic_year')
        if academic_year:
            form = MasterForm(initial={'academic_year': academic_year})

        context = {
            "page_title": "Create new School Year Subject",
            "menu_section": "admin_dashboard",
            "menu_subsection": "academic_year_subject",
            "menu_action": "create",
            "form": form
        }

        return render(request, "admin_dashboard/academic_year_subjects/form.html", context)
    
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
                    'admin_dashboard_academic_year_subjects_detail',
                    kwargs={
                        'academic_year_subject': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new School Year Subject",
                "menu_section": "admin_dashboard",
                "menu_subsection": "academic_year_subject",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "admin_dashboard/academic_year_subjects/form.html", context)


class AdminDashboardAcademicYearSubjectDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Academic Year Subjects. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('academic_year_subject', None))
        context = {
            "page_title": f"School Year Subject: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "academic_year_subject",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "admin_dashboard/academic_year_subjects/detail.html", context)


class AdminDashboardAcademicYearSubjectUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Academic Year Subjects. 
    
    Allowed HTTP verbs: 
        - GET
        - POST
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('academic_year_subject', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update School Year Subject: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "academic_year_subject",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "admin_dashboard/academic_year_subjects/form.html", context)
    
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
                    'admin_dashboard_academic_year_subjects_detail',
                    kwargs={
                        'academic_year_subject': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update School Year Subject: {obj}",
                "menu_section": "admin_dashboard",
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
            return render(request, "admin_dashboard/academic_year_subjects/form.html", context)


class AdminDashboardAcademicYearSubjectDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Academic Year Subjects. 
    
    Allowed HTTP verbs: 
        - GET
        - POST
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('academic_year_subject', None))
        context = {
            "page_title": "Delete School Year Subject: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "academic_year_subject",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "admin_dashboard/academic_year_subjects/delete.html", context)
    
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
                'admin_dashboard_academic_year_subjects_list'
            )
        )
