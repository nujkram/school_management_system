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

from subjects.models.subject.models import Subject as Master
from admin_dashboard.controllers.views.admin_dashboard.subjects.forms import SubjectForm as MasterForm

"""
URLS
# Subject

from admin_dashboard.controllers.views.admin_dashboard.subjects import main as subjects_views

urlpatterns += [
    path(
        'subject/list',
        subjects_views.AdminDashboardSubjectListView.as_view(),
        name='admin_dashboard_subjects_list'
    ),
    path(
        'subject/<subject>/detail',
        subjects_views.AdminDashboardSubjectDetailView.as_view(),
        name='admin_dashboard_subjects_detail'
    ),
    path(
        'subject/create',
        subjects_views.AdminDashboardSubjectCreateView.as_view(),
        name='admin_dashboard_subjects_create'
    ),
    path(
        'subject/<subject>/update',
        subjects_views.AdminDashboardSubjectUpdateView.as_view(),
        name='admin_dashboard_subjects_update'
    ),
    path(
        'subject/<subject>/delete',
        subjects_views.AdminDashboardSubjectDeleteView.as_view(),
        name='admin_dashboard_subjects_delete'
    )
]
"""


class AdminDashboardSubjectListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    List view for Subjects. 
    
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
            "page_title": f"Subjects",
            "menu_section": "admin_dashboard",
            "menu_subsection": "subject",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "admin_dashboard/subjects/list.html", context)


class AdminDashboardSubjectCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Subjects. 
    
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
            "page_title": "Create new Subject",
            "menu_section": "admin_dashboard",
            "menu_subsection": "subject",
            "menu_action": "create",
            "form": form
        }

        return render(request, "admin_dashboard/subjects/form.html", context)
    
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
                    'admin_dashboard_subjects_detail',
                    kwargs={
                        'subject': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Subject",
                "menu_section": "admin_dashboard",
                "menu_subsection": "subject",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "admin_dashboard/subjects/form.html", context)


class AdminDashboardSubjectDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Subjects. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('subject', None))
        context = {
            "page_title": f"Subject: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "subject",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "admin_dashboard/subjects/detail.html", context)


class AdminDashboardSubjectUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Subjects. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('subject', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Subject: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "subject",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "admin_dashboard/subjects/form.html", context)
    
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
                    'admin_dashboard_subjects_detail',
                    kwargs={
                        'subject': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Subject: {obj}",
                "menu_section": "admin_dashboard",
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
            return render(request, "admin_dashboard/subjects/form.html", context)


class AdminDashboardSubjectDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Subjects. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('subject', None))
        context = {
            "page_title": f"Delete Subject: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "subject",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "admin_dashboard/subjects/delete.html", context)
    
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
                'admin_dashboard_subjects_list'
            )
        )
