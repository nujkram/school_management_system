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

from academic_years.models import AcademicYearSubject
from accounts.mixins.user_type_mixins import IsStudentViewMixin
from subjects.models import Subject

from topics.models.topic.models import Topic as Master
from student_dashboard.controllers.views.student_dashboard.topics.forms import TopicForm as MasterForm

"""
URLS
# Topic

from student_dashboard.controllers.views.student_dashboard.topics import main as topics_views

urlpatterns += [
    path(
        'topic/list',
        topics_views.StudentDashboardTopicListView.as_view(),
        name='student_dashboard_topics_list'
    ),
    path(
        'topic/<topic>/detail',
        topics_views.StudentDashboardTopicDetailView.as_view(),
        name='student_dashboard_topics_detail'
    ),
    path(
        'topic/create',
        topics_views.StudentDashboardTopicCreateView.as_view(),
        name='student_dashboard_topics_create'
    ),
    path(
        'topic/<topic>/update',
        topics_views.StudentDashboardTopicUpdateView.as_view(),
        name='student_dashboard_topics_update'
    ),
    path(
        'topic/<topic>/delete',
        topics_views.StudentDashboardTopicDeleteView.as_view(),
        name='student_dashboard_topics_delete'
    )
]
"""


class StudentDashboardTopicListView(LoginRequiredMixin, IsStudentViewMixin, View):
    """ 
    List view for Topics. 
    
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
        obj_list = Master.objects.actives().order_by('created')
        paginator = Paginator(obj_list, 50)
        page = request.GET.get('page')
        objs = paginator.get_page(page)
        try:
            academic_year_subject = AcademicYearSubject.objects.get(pk=kwargs.get('academic_year_subject'))
            subject = Subject.objects.get(pk=academic_year_subject.subject.pk)
        except AcademicYearSubject.DoesNotExist:
            academic_year_subject = 'None'
            subject = 'None'

        context = {
            "page_title": f"Topics",
            "menu_section": "student_dashboard",
            "menu_subsection": "topic",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs,
            "academic_year_subject": academic_year_subject,
            "subject": subject,
        }

        return render(request, "student_dashboard/topics/list.html", context)


class StudentDashboardTopicCreateView(LoginRequiredMixin, IsStudentViewMixin, View):
    """ 
    Create view for Topics. 
    
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
            "page_title": "Create new Topic",
            "menu_section": "student_dashboard",
            "menu_subsection": "topic",
            "menu_action": "create",
            "form": form
        }

        return render(request, "student_dashboard/topics/form.html", context)
    
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
                    'student_dashboard_topics_detail',
                    kwargs={
                        'topic': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Topic",
                "menu_section": "student_dashboard",
                "menu_subsection": "topic",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "student_dashboard/topics/form.html", context)


class StudentDashboardTopicDetailView(LoginRequiredMixin, IsStudentViewMixin, View):
    """ 
    Create view for Topics. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - Student user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('topic', None))
        context = {
            "page_title": f"Topic: {obj}",
            "menu_section": "student_dashboard",
            "menu_subsection": "topic",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "student_dashboard/topics/detail.html", context)


class StudentDashboardTopicUpdateView(LoginRequiredMixin, IsStudentViewMixin, View):
    """ 
    Create view for Topics. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('topic', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Topic: {obj}",
            "menu_section": "student_dashboard",
            "menu_subsection": "topic",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "student_dashboard/topics/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('topic', None))
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
                    'student_dashboard_topics_detail',
                    kwargs={
                        'topic': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Topic: {obj}",
                "menu_section": "student_dashboard",
                "menu_subsection": "topic",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "student_dashboard/topics/form.html", context)


class StudentDashboardTopicDeleteView(LoginRequiredMixin, IsStudentViewMixin, View):
    """ 
    Create view for Topics. 
    
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
        obj = get_object_or_404(Master, pk=kwargs.get('topic', None))
        context = {
            "page_title": "Delete Topic: {obj}",
            "menu_section": "student_dashboard",
            "menu_subsection": "topic",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "student_dashboard/topics/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('topic', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'student_dashboard_topics_list'
            )
        )
