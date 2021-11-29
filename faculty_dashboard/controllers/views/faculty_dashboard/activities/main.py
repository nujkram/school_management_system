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

from accounts.mixins.user_type_mixins import IsFacultyViewMixin

from activities.models.activity.models import Activity as Master
from faculty_dashboard.controllers.views.faculty_dashboard.activities.forms import ActivityForm as MasterForm
from topics.models import Topic

"""
URLS
# Activity

from faculty_dashboard.controllers.views.faculty_dashboard.activities import main as activities_views

urlpatterns += [
    path(
        'activity/list',
        activities_views.FacultyDashboardActivityListView.as_view(),
        name='faculty_dashboard_activities_list'
    ),
    path(
        'activity/<activity>/detail',
        activities_views.FacultyDashboardActivityDetailView.as_view(),
        name='faculty_dashboard_activities_detail'
    ),
    path(
        'activity/create',
        activities_views.FacultyDashboardActivityCreateView.as_view(),
        name='faculty_dashboard_activities_create'
    ),
    path(
        'activity/<activity>/update',
        activities_views.FacultyDashboardActivityUpdateView.as_view(),
        name='faculty_dashboard_activities_update'
    ),
    path(
        'activity/<activity>/delete',
        activities_views.FacultyDashboardActivityDeleteView.as_view(),
        name='faculty_dashboard_activities_delete'
    )
]
"""


class FacultyDashboardActivityListView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    List view for Activities. 
    
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
            "page_title": f"Activities",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "activity",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "faculty_dashboard/activities/list.html", context)


class FacultyDashboardActivityCreateView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Activities. 
    
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
        topic = Topic.objects.get(pk=request.GET.get('topic'))
        form = MasterForm(initial={'topic': topic.pk})
        context = {
            "page_title": "Create new Activity",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "activity",
            "menu_action": "create",
            "form": form,
            "topic": topic,
        }

        return render(request, "faculty_dashboard/activities/form.html", context)
    
    def post(self, request, *args, **kwargs):
        form = MasterForm(data=request.POST, files=request.FILES)

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
                    'faculty_dashboard_activities_detail',
                    kwargs={
                        'activity': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Activity",
                "menu_section": "faculty_dashboard",
                "menu_subsection": "activity",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "faculty_dashboard/activities/form.html", context)


class FacultyDashboardActivityDetailView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Activities. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Faculty user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('activity', None))
        context = {
            "page_title": f"Activity: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "activity",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "faculty_dashboard/activities/detail.html", context)


class FacultyDashboardActivityUpdateView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Activities. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('activity', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Activity: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "activity",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "faculty_dashboard/activities/form.html", context)
    
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
                    'faculty_dashboard_activities_detail',
                    kwargs={
                        'activity': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Activity: {obj}",
                "menu_section": "faculty_dashboard",
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
            return render(request, "faculty_dashboard/activities/form.html", context)


class FacultyDashboardActivityDeleteView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Activities. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('activity', None))
        context = {
            "page_title": "Delete Activity: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "activity",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "faculty_dashboard/activities/delete.html", context)
    
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
                'faculty_dashboard_activities_list'
            )
        )
