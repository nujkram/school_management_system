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

from exercises.models.exercise.models import Exercise as Master
from faculty_dashboard.controllers.views.faculty_dashboard.exercises.forms import ExerciseForm as MasterForm

"""
URLS
# Exercise

from faculty_dashboard.controllers.views.faculty_dashboard.exercises import main as exercises_views

urlpatterns += [
    path(
        'exercise/list',
        exercises_views.FacultyDashboardExerciseListView.as_view(),
        name='faculty_dashboard_exercises_list'
    ),
    path(
        'exercise/<exercise>/detail',
        exercises_views.FacultyDashboardExerciseDetailView.as_view(),
        name='faculty_dashboard_exercises_detail'
    ),
    path(
        'exercise/create',
        exercises_views.FacultyDashboardExerciseCreateView.as_view(),
        name='faculty_dashboard_exercises_create'
    ),
    path(
        'exercise/<exercise>/update',
        exercises_views.FacultyDashboardExerciseUpdateView.as_view(),
        name='faculty_dashboard_exercises_update'
    ),
    path(
        'exercise/<exercise>/delete',
        exercises_views.FacultyDashboardExerciseDeleteView.as_view(),
        name='faculty_dashboard_exercises_delete'
    )
]
"""


class FacultyDashboardExerciseListView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    List view for Exercises. 
    
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
        obj_list = Master.objects.filter(activity=kwargs.get('activity'))
        paginator = Paginator(obj_list, 50)
        page = request.GET.get('page')
        objs = paginator.get_page(page)

        context = {
            "page_title": f"Exercises",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "exercise",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "faculty_dashboard/exercises/list.html", context)


class FacultyDashboardExerciseCreateView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Exercises. 
    
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
            "page_title": "Create new Exercise",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "exercise",
            "menu_action": "create",
            "form": form
        }

        return render(request, "faculty_dashboard/exercises/form.html", context)
    
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
                    'faculty_dashboard_exercises_detail',
                    kwargs={
                        'exercise': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Exercise",
                "menu_section": "faculty_dashboard",
                "menu_subsection": "exercise",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "faculty_dashboard/exercises/form.html", context)


class FacultyDashboardExerciseDetailView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Exercises. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Faculty user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('exercise', None))
        context = {
            "page_title": f"Exercise: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "exercise",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "faculty_dashboard/exercises/detail.html", context)


class FacultyDashboardExerciseUpdateView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Exercises. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('exercise', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Exercise: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "exercise",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "faculty_dashboard/exercises/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('exercise', None))
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
                    'faculty_dashboard_exercises_detail',
                    kwargs={
                        'exercise': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Exercise: {obj}",
                "menu_section": "faculty_dashboard",
                "menu_subsection": "exercise",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "faculty_dashboard/exercises/form.html", context)


class FacultyDashboardExerciseDeleteView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """ 
    Create view for Exercises. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('exercise', None))
        context = {
            "page_title": "Delete Exercise: {obj}",
            "menu_section": "faculty_dashboard",
            "menu_subsection": "exercise",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "faculty_dashboard/exercises/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('exercise', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'faculty_dashboard_exercises_list'
            )
        )
