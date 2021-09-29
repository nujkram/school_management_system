"""
School Management System Project
Description for School Management System Project

Author: empty
Version: 0.0.1
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from accounts.mixins.user_type_mixins import IsFacultyViewMixin


class StudentDashboardHomeView(LoginRequiredMixin, IsFacultyViewMixin, View):
    """
    Faculty Dashboard Home.

    Allowed HTTP verbs:
        - GET

    Restrictions:
        - LoginRequired
        - Admin user

    """

    def get(self, request, *args, **kwargs):

        context = {
            "page_title": f"Student Dashboard",
            "menu_section": "student_dashboard",
            "menu_subsection": "student_dashboard",
            "menu_action": "home",
        }

        return render(request, "student_dashboard/home/home.html", context)
