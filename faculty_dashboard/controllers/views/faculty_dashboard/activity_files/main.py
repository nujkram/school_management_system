"""
School Management System
Description for School Management System

Author: Empty (empty@gmail.com)
Version: 0.0.1
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from accounts.mixins.user_type_mixins import IsFacultyViewMixin
from activities.models import Activity

from activity_files.models.activity_file.models import ActivityFile as Master, ActivityFile
from faculty_dashboard.controllers.views.faculty_dashboard.activity_files.forms import ActivityFileForm as MasterForm

"""
URLS
# Activity File

from faculty_dashboard.controllers.views.faculty_dashboard.activity_files import main as activity_files_views

urlpatterns += [
    path(
        'activity_file/list',
        activity_files_views.FacultyDashboardActivityFileListView.as_view(),
        name='faculty_dashboard_activity_files_list'
    ),
    path(
        'activity_file/<activity_file>/detail',
        activity_files_views.FacultyDashboardActivityFileDetailView.as_view(),
        name='faculty_dashboard_activity_files_detail'
    ),
    path(
        'activity_file/create',
        activity_files_views.FacultyDashboardActivityFileCreateView.as_view(),
        name='faculty_dashboard_activity_files_create'
    ),
    path(
        'activity_file/<activity_file>/update',
        activity_files_views.FacultyDashboardActivityFileUpdateView.as_view(),
        name='faculty_dashboard_activity_files_update'
    ),
    path(
        'activity_file/<activity_file>/delete',
        activity_files_views.FacultyDashboardActivityFileDeleteView.as_view(),
        name='faculty_dashboard_activity_files_delete'
    )
]
"""


class FacultyDashboardActivityFileListView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    List view for Activity Files. 
    
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
            "page_title": f"Activity Files",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "activity_file",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "faculty_dashboard/activity_files/list.html", context)


class FacultyDashboardActivityFileCreateView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Activity Files. 
    
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
        activity_pk = request.GET.get('activity')
        activity = Activity.objects.get(pk=activity_pk)
        files = ActivityFile.objects.filter(activity=activity)
        print(files)
        print(files.count())
        context = {
            "page_title": "Upload new activity file",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "activity_file",
            "menu_action": "create",
            "form": form,
            "activity": activity_pk,
            "files": files,
        }

        return render(request, "faculty_dashboard/activity_files/form.html", context)

    def post(self, request, *args, **kwargs):
        # https://simpleisbetterthancomplex.com/tutorial/2016/11/22/django-multiple-file-upload-using-ajax.html
        form = MasterForm(data=request.POST, files=request.FILES)
        activity = Activity.objects.get(pk=request.GET.get('activity'))
        if form.is_valid():
            data = form.save(commit=False)
            data.updated_by = request.user
            data.activity = activity
            data = form.save()
            files = {'is_valid': True, 'attached_file': data.attached_file.name, 'url': data.attached_file.url}

        else:
            files = {'is_valid': False}

        return JsonResponse(files)


class FacultyDashboardActivityFileDetailView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Activity Files. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Faculty user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('activity_file', None))
        context = {
            "page_title": f"Activity File: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "activity_file",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "faculty_dashboard/activity_files/detail.html", context)


class FacultyDashboardActivityFileUpdateView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Activity Files. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('activity_file', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Activity File: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "activity_file",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "faculty_dashboard/activity_files/form.html", context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('activity_file', None))
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
                    'faculty_dashboard_activity_files_detail',
                    kwargs={
                        'activity_file': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Activity File: {obj}",
                "menu_section": "faculty_dashboard",
                "menu_subsection": "activity_file",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "faculty_dashboard/activity_files/form.html", context)


class FacultyDashboardActivityFileDeleteView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Activity Files. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('activity_file', None))
        context = {
            "page_title": "Delete Activity File: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "activity_file",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "faculty_dashboard/activity_files/delete.html", context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('activity_file', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'faculty_dashboard_activity_files_list'
            )
        )
