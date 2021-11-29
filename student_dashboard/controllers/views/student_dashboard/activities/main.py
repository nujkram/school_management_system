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

from accounts.mixins.user_type_mixins import IsStudentViewMixin

from activities.models.activity.models import Activity as Master
from student_dashboard.controllers.views.student_dashboard.activities.forms import ActivityForm as MasterForm

"""
URLS
# Activity

from student_dashboard.controllers.views.student_dashboard.activities import main as activities_views

urlpatterns += [
    path(
        'activity/list',
        activities_views.StudentDashboardActivityListView.as_view(),
        name='student_dashboard_activities_list'
    ),
    path(
        'activity/<activity>/detail',
        activities_views.StudentDashboardActivityDetailView.as_view(),
        name='student_dashboard_activities_detail'
    ),
    path(
        'activity/create',
        activities_views.StudentDashboardActivityCreateView.as_view(),
        name='student_dashboard_activities_create'
    ),
    path(
        'activity/<activity>/update',
        activities_views.StudentDashboardActivityUpdateView.as_view(),
        name='student_dashboard_activities_update'
    ),
    path(
        'activity/<activity>/delete',
        activities_views.StudentDashboardActivityDeleteView.as_view(),
        name='student_dashboard_activities_delete'
    )
]
"""


class StudentDashboardActivityListView(LoginRequiredMixin, IsStudentViewMixin, View):
    """ 
    List view for Activities. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Student user

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
            "page_title": f"Activities",
            "menu_section": "student_dashboard",
            "menu_subsection": "activity",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "student_dashboard/activities/list.html", context)


class StudentDashboardActivityCreateView(LoginRequiredMixin, IsStudentViewMixin, View):
    """ 
    Create view for Activities. 
    
    Allowed HTTP verbs: 
        - GET
        - POST
    
    Restrictions:
        - LoginRequired
        - Student user

    Filters:
        - Optionally used more multi-user/multi-tenant apps to separate ownership
        - ex: company=kwargs.get('company')
    """

    def get(self, request, *args, **kwargs):
        form = MasterForm
        context = {
            "page_title": "Create new Activity",
            "menu_section": "student_dashboard",
            "menu_subsection": "activity",
            "menu_action": "create",
            "form": form
        }

        return render(request, "student_dashboard/activities/form.html", context)
    
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
                    'student_dashboard_activities_detail',
                    kwargs={
                        'activity': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Activity",
                "menu_section": "student_dashboard",
                "menu_subsection": "activity",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "student_dashboard/activities/form.html", context)


class StudentDashboardActivityDetailView(LoginRequiredMixin, IsStudentViewMixin, View):
    """ 
    Create view for Activities. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Student user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('activity', None))
        context = {
            "page_title": f"Activity: {obj}",
            "menu_section": "student_dashboard",
            "menu_subsection": "activity",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "student_dashboard/activities/detail.html", context)


class StudentDashboardActivityUpdateView(LoginRequiredMixin, IsStudentViewMixin, View):
    """ 
    Create view for Activities. 
    
    Allowed HTTP verbs: 
        - GET
        - POST
    
    Restrictions:
        - LoginRequired
        - Student user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('activity', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Activity: {obj}",
            "menu_section": "student_dashboard",
            "menu_subsection": "activity",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "student_dashboard/activities/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('activity', None))
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
                    'student_dashboard_activities_detail',
                    kwargs={
                        'activity': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Activity: {obj}",
                "menu_section": "student_dashboard",
                "menu_subsection": "activity",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "student_dashboard/activities/form.html", context)


class StudentDashboardActivityDeleteView(LoginRequiredMixin, IsStudentViewMixin, View):
    """ 
    Create view for Activities. 
    
    Allowed HTTP verbs: 
        - GET
        - POST
    
    Restrictions:
        - LoginRequired
        - Student user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('activity', None))
        context = {
            "page_title": "Delete Activity: {obj}",
            "menu_section": "student_dashboard",
            "menu_subsection": "activity",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "student_dashboard/activities/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('activity', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'student_dashboard_activities_list'
            )
        )
