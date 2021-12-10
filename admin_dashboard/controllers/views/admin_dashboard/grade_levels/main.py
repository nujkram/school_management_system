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

from grade_levels.models.grade_level.models import GradeLevel as Master
from admin_dashboard.controllers.views.admin_dashboard.grade_levels.forms import GradeLevelForm as MasterForm

"""
URLS
# Grade Level

from admin_dashboard.controllers.views.admin_dashboard.grade_levels import main as grade_levels_views

urlpatterns += [
    path(
        'grade_level/list',
        grade_levels_views.AdminDashboardGradeLevelListView.as_view(),
        name='admin_dashboard_grade_levels_list'
    ),
    path(
        'grade_level/<grade_level>/detail',
        grade_levels_views.AdminDashboardGradeLevelDetailView.as_view(),
        name='admin_dashboard_grade_levels_detail'
    ),
    path(
        'grade_level/create',
        grade_levels_views.AdminDashboardGradeLevelCreateView.as_view(),
        name='admin_dashboard_grade_levels_create'
    ),
    path(
        'grade_level/<grade_level>/update',
        grade_levels_views.AdminDashboardGradeLevelUpdateView.as_view(),
        name='admin_dashboard_grade_levels_update'
    ),
    path(
        'grade_level/<grade_level>/delete',
        grade_levels_views.AdminDashboardGradeLevelDeleteView.as_view(),
        name='admin_dashboard_grade_levels_delete'
    )
]
"""


class AdminDashboardGradeLevelListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    List view for Grade Levels. 
    
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
            "page_title": f"Grade Levels",
            "menu_section": "admin_dashboard",
            "menu_subsection": "grade_level",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "admin_dashboard/grade_levels/list.html", context)


class AdminDashboardGradeLevelCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Grade Levels. 
    
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
            "page_title": "Create new Grade Level",
            "menu_section": "admin_dashboard",
            "menu_subsection": "grade_level",
            "menu_action": "create",
            "form": form
        }

        return render(request, "admin_dashboard/grade_levels/form.html", context)
    
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
                    'admin_dashboard_grade_levels_detail',
                    kwargs={
                        'grade_level': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Grade Level",
                "menu_section": "admin_dashboard",
                "menu_subsection": "grade_level",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "admin_dashboard/grade_levels/form.html", context)


class AdminDashboardGradeLevelDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Grade Levels. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('grade_level', None))
        context = {
            "page_title": f"Grade Level: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "grade_level",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "admin_dashboard/grade_levels/detail.html", context)


class AdminDashboardGradeLevelUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Grade Levels. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('grade_level', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Grade Level: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "grade_level",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "admin_dashboard/grade_levels/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('grade_level', None))
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
                    'admin_dashboard_grade_levels_detail',
                    kwargs={
                        'grade_level': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Grade Level: {obj}",
                "menu_section": "admin_dashboard",
                "menu_subsection": "grade_level",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "admin_dashboard/grade_levels/form.html", context)


class AdminDashboardGradeLevelDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Grade Levels. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('grade_level', None))
        context = {
            "page_title": f"Delete Grade Level: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "grade_level",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "admin_dashboard/grade_levels/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('grade_level', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'admin_dashboard_grade_levels_list'
            )
        )
