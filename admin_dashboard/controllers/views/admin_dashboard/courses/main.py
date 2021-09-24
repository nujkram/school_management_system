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

from courses.models.course.models import Course as Master
from admin_dashboard.controllers.views.admin_dashboard.courses.forms import CourseForm as MasterForm

"""
URLS
# Course

from admin_dashboard.controllers.views.admin_dashboard.courses import main as courses_views

urlpatterns += [
    path(
        'course/list',
        courses_views.AdminDashboardCourseListView.as_view(),
        name='admin_dashboard_courses_list'
    ),
    path(
        'course/<course>/detail',
        courses_views.AdminDashboardCourseDetailView.as_view(),
        name='admin_dashboard_courses_detail'
    ),
    path(
        'course/create',
        courses_views.AdminDashboardCourseCreateView.as_view(),
        name='admin_dashboard_courses_create'
    ),
    path(
        'course/<course>/update',
        courses_views.AdminDashboardCourseUpdateView.as_view(),
        name='admin_dashboard_courses_update'
    ),
    path(
        'course/<course>/delete',
        courses_views.AdminDashboardCourseDeleteView.as_view(),
        name='admin_dashboard_courses_delete'
    )
]
"""


class AdminDashboardCourseListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    List view for Courses. 
    
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
            "page_title": f"Courses",
            "menu_section": "admin_dashboard",
            "menu_subsection": "course",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "admin_dashboard/courses/list.html", context)


class AdminDashboardCourseCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Courses. 
    
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
            "page_title": "Create new Course",
            "menu_section": "admin_dashboard",
            "menu_subsection": "course",
            "menu_action": "create",
            "form": form
        }

        return render(request, "admin_dashboard/courses/form.html", context)
    
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
                    'admin_dashboard_courses_detail',
                    kwargs={
                        'course': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Course",
                "menu_section": "admin_dashboard",
                "menu_subsection": "course",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "admin_dashboard/courses/form.html", context)


class AdminDashboardCourseDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Courses. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('course', None))
        context = {
            "page_title": f"Course: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "course",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "admin_dashboard/courses/detail.html", context)


class AdminDashboardCourseUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Courses. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('course', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Course: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "course",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "admin_dashboard/courses/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('course', None))
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
                    'admin_dashboard_courses_detail',
                    kwargs={
                        'course': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Course: {obj}",
                "menu_section": "admin_dashboard",
                "menu_subsection": "course",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "admin_dashboard/courses/form.html", context)


class AdminDashboardCourseDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """ 
    Create view for Courses. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('course', None))
        context = {
            "page_title": "Delete Course: {obj}",
            "menu_section": "admin_dashboard",
            "menu_subsection": "course",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "admin_dashboard/courses/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('course', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'admin_dashboard_courses_list'
            )
        )
