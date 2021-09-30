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

from year_levels.models.year_level.models import YearLevel as Master
from admin_dashboard.controllers.views.admin_dashboard.year_levels.forms import YearLevelForm as MasterForm

"""
URLS
# Year Level

from admin_dashboard.controllers.views.admin_dashboard.year_levels import main as year_levels_views

urlpatterns += [
    path(
        'year_level/list',
        year_levels_views.AdminDashboardYearLevelListView.as_view(),
        name='admin_dashboard_year_levels_list'
    ),
    path(
        'year_level/<year_level>/detail',
        year_levels_views.AdminDashboardYearLevelDetailView.as_view(),
        name='admin_dashboard_year_levels_detail'
    ),
    path(
        'year_level/create',
        year_levels_views.AdminDashboardYearLevelCreateView.as_view(),
        name='admin_dashboard_year_levels_create'
    ),
    path(
        'year_level/<year_level>/update',
        year_levels_views.AdminDashboardYearLevelUpdateView.as_view(),
        name='admin_dashboard_year_levels_update'
    ),
    path(
        'year_level/<year_level>/delete',
        year_levels_views.AdminDashboardYearLevelDeleteView.as_view(),
        name='admin_dashboard_year_levels_delete'
    )
]
"""


class AdminDashboardYearLevelListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    List view for Year Levels. 
    
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
            "page_title": f"Year Levels",
            "menu_section": "admin_dashboard",
            "menu_subsection": "year_level",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "admin_dashboard/year_levels/list.html", context)


class AdminDashboardYearLevelCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Year Levels. 
    
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
            "page_title": "Create new Year Level",
            "menu_section": "admin_dashboard",
            "menu_subsection": "year_level",
            "menu_action": "create",
            "form": form
        }

        return render(request, "admin_dashboard/year_levels/form.html", context)
    
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
                    'admin_dashboard_year_levels_detail',
                    kwargs={
                        'year_level': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Year Level",
                "menu_section": "admin_dashboard",
                "menu_subsection": "year_level",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "admin_dashboard/year_levels/form.html", context)


class AdminDashboardYearLevelDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Year Levels. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('year_level', None))
        context = {
            "page_title": f"Year Level: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "year_level",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "admin_dashboard/year_levels/detail.html", context)


class AdminDashboardYearLevelUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Year Levels. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('year_level', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Year Level: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "year_level",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "admin_dashboard/year_levels/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('year_level', None))
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
                    'admin_dashboard_year_levels_detail',
                    kwargs={
                        'year_level': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Year Level: {obj}",
                "menu_section": "admin_dashboard",
                "menu_subsection": "year_level",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "admin_dashboard/year_levels/form.html", context)


class AdminDashboardYearLevelDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Year Levels. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('year_level', None))
        context = {
            "page_title": "Delete Year Level: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "year_level",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "admin_dashboard/year_levels/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('year_level', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'admin_dashboard_year_levels_list'
            )
        )
