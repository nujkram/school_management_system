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

from academic_years.models.academic_year.models import AcademicYear as Master
from student_dashboard.controllers.views.student_dashboard.academic_years.forms import AcademicYearForm as MasterForm

"""
URLS
# Academic Year

from student_dashboard.controllers.views.student_dashboard.academic_years import main as academic_years_views

urlpatterns += [
    path(
        'academic_year/list',
        academic_years_views.StudentDashboardAcademicYearListView.as_view(),
        name='student_dashboard_academic_years_list'
    ),
    path(
        'academic_year/<academic_year>/detail',
        academic_years_views.StudentDashboardAcademicYearDetailView.as_view(),
        name='student_dashboard_academic_years_detail'
    ),
    path(
        'academic_year/create',
        academic_years_views.StudentDashboardAcademicYearCreateView.as_view(),
        name='student_dashboard_academic_years_create'
    ),
    path(
        'academic_year/<academic_year>/update',
        academic_years_views.StudentDashboardAcademicYearUpdateView.as_view(),
        name='student_dashboard_academic_years_update'
    ),
    path(
        'academic_year/<academic_year>/delete',
        academic_years_views.StudentDashboardAcademicYearDeleteView.as_view(),
        name='student_dashboard_academic_years_delete'
    )
]
"""


class StudentDashboardAcademicYearListView(LoginRequiredMixin, IsStudentViewMixin, View):
    """ 
    List view for Academic Years. 
    
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
            "page_title": f"School Years",
            "menu_section": "student_dashboard",
            "menu_subsection": "academic_year",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "student_dashboard/academic_years/list.html", context)


class StudentDashboardAcademicYearCreateView(LoginRequiredMixin, IsStudentViewMixin, View):
    """ 
    Create view for Academic Years. 
    
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
            "page_title": "Create new School Year",
            "menu_section": "student_dashboard",
            "menu_subsection": "academic_year",
            "menu_action": "create",
            "form": form
        }

        return render(request, "student_dashboard/academic_years/form.html", context)
    
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
                    'student_dashboard_academic_years_detail',
                    kwargs={
                        'academic_year': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new School Year",
                "menu_section": "student_dashboard",
                "menu_subsection": "academic_year",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "student_dashboard/academic_years/form.html", context)


class StudentDashboardAcademicYearDetailView(LoginRequiredMixin, IsStudentViewMixin, View):
    """ 
    Create view for Academic Years. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Student user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('academic_year', None))
        context = {
            "page_title": f"School Year: {obj}",
            "menu_section": "student_dashboard",
            "menu_subsection": "academic_year",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "student_dashboard/academic_years/detail.html", context)


class StudentDashboardAcademicYearUpdateView(LoginRequiredMixin, IsStudentViewMixin, View):
    """ 
    Create view for Academic Years. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('academic_year', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update School Year: {obj}",
            "menu_section": "student_dashboard",
            "menu_subsection": "academic_year",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "student_dashboard/academic_years/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('academic_year', None))
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
                    'student_dashboard_academic_years_detail',
                    kwargs={
                        'academic_year': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update School Year: {obj}",
                "menu_section": "student_dashboard",
                "menu_subsection": "academic_year",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "student_dashboard/academic_years/form.html", context)


class StudentDashboardAcademicYearDeleteView(LoginRequiredMixin, IsStudentViewMixin, View):
    """ 
    Create view for Academic Years. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('academic_year', None))
        context = {
            "page_title": "Delete School Year: {obj}",
            "menu_section": "student_dashboard",
            "menu_subsection": "academic_year",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "student_dashboard/academic_years/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('academic_year', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'student_dashboard_academic_years_list'
            )
        )
