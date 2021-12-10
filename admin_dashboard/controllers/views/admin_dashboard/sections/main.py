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

from sections.models.section.models import Section as Master
from admin_dashboard.controllers.views.admin_dashboard.sections.forms import SectionForm as MasterForm

"""
URLS
# Section

from admin_dashboard.controllers.views.admin_dashboard.sections import main as sections_views

urlpatterns += [
    path(
        'section/list',
        sections_views.AdminDashboardSectionListView.as_view(),
        name='admin_dashboard_sections_list'
    ),
    path(
        'section/<section>/detail',
        sections_views.AdminDashboardSectionDetailView.as_view(),
        name='admin_dashboard_sections_detail'
    ),
    path(
        'section/create',
        sections_views.AdminDashboardSectionCreateView.as_view(),
        name='admin_dashboard_sections_create'
    ),
    path(
        'section/<section>/update',
        sections_views.AdminDashboardSectionUpdateView.as_view(),
        name='admin_dashboard_sections_update'
    ),
    path(
        'section/<section>/delete',
        sections_views.AdminDashboardSectionDeleteView.as_view(),
        name='admin_dashboard_sections_delete'
    )
]
"""


class AdminDashboardSectionListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    List view for Sections. 
    
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
            "page_title": f"Sections",
            "menu_section": "admin_dashboard",
            "menu_subsection": "section",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "admin_dashboard/sections/list.html", context)


class AdminDashboardSectionCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Sections. 
    
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
            "page_title": "Create new Section",
            "menu_section": "admin_dashboard",
            "menu_subsection": "section",
            "menu_action": "create",
            "form": form
        }

        return render(request, "admin_dashboard/sections/form.html", context)
    
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
                    'admin_dashboard_sections_detail',
                    kwargs={
                        'section': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Section",
                "menu_section": "admin_dashboard",
                "menu_subsection": "section",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "admin_dashboard/sections/form.html", context)


class AdminDashboardSectionDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Sections. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('section', None))
        context = {
            "page_title": f"Section: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "section",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "admin_dashboard/sections/detail.html", context)


class AdminDashboardSectionUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Sections. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('section', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Section: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "section",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "admin_dashboard/sections/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('section', None))
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
                    'admin_dashboard_sections_detail',
                    kwargs={
                        'section': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Section: {obj}",
                "menu_section": "admin_dashboard",
                "menu_subsection": "section",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "admin_dashboard/sections/form.html", context)


class AdminDashboardSectionDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Sections. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('section', None))
        context = {
            "page_title": f"Delete Section: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "section",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "sections/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('section', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'admin_dashboard_sections_list'
            )
        )
