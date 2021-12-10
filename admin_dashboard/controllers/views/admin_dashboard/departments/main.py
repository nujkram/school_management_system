"""
School Management System
Description for School Management System

Author: Christian Arellado (christianarellado@gmail.com)
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

from departments.models.department.models import Department as Master
from admin_dashboard.controllers.views.admin_dashboard.departments.forms import DepartmentForm as MasterForm

"""
URLS
# Department

from admin_dashboard.controllers.views.admin_dashboard.departments import main as departments_views

urlpatterns += [
    path(
        'department/list',
        departments_views.AdminDashboardDepartmentListView.as_view(),
        name='admin_dashboard_departments_list'
    ),
    path(
        'department/<department>/detail',
        departments_views.AdminDashboardDepartmentDetailView.as_view(),
        name='admin_dashboard_departments_detail'
    ),
    path(
        'department/create',
        departments_views.AdminDashboardDepartmentCreateView.as_view(),
        name='admin_dashboard_departments_create'
    ),
    path(
        'department/<department>/update',
        departments_views.AdminDashboardDepartmentUpdateView.as_view(),
        name='admin_dashboard_departments_update'
    ),
    path(
        'department/<department>/delete',
        departments_views.AdminDashboardDepartmentDeleteView.as_view(),
        name='admin_dashboard_departments_delete'
    )
]
"""


class AdminDashboardDepartmentListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    List view for Departments. 
    
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
        obj_list = Master.objects.actives()
        paginator = Paginator(obj_list, 50)
        page = request.GET.get('page')
        objs = paginator.get_page(page)

        context = {
            "page_title": f"Departments",
            "menu_section": "admin_dashboard",
            "menu_subsection": "department",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "admin_dashboard/departments/list.html", context)


class AdminDashboardDepartmentCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Departments. 
    
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
        form = MasterForm
        context = {
            "page_title": "Create new Department",
            "menu_section": "admin_dashboard",
            "menu_subsection": "department",
            "menu_action": "create",
            "form": form
        }

        return render(request, "admin_dashboard/departments/form.html", context)
    
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
                    'admin_dashboard_departments_detail',
                    kwargs={
                        'department': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Department",
                "menu_section": "admin_dashboard",
                "menu_subsection": "department",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "admin_dashboard/departments/form.html", context)


class AdminDashboardDepartmentDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Departments. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('department', None))
        context = {
            "page_title": f"Department: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "department",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "admin_dashboard/departments/detail.html", context)


class AdminDashboardDepartmentUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Departments. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('department', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Department: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "department",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "admin_dashboard/departments/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('department', None))
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
                    'admin_dashboard_departments_detail',
                    kwargs={
                        'department': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Department: {obj}",
                "menu_section": "admin_dashboard",
                "menu_subsection": "department",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "admin_dashboard/departments/form.html", context)


class AdminDashboardDepartmentDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Departments. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('department', None))
        context = {
            "page_title": f"Delete Department: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "department",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "admin_dashboard/departments/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('department', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'admin_dashboard_departments_list'
            )
        )
