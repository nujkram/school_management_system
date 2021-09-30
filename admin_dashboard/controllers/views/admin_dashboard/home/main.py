"""
School Management System Project
Description for School Management System Project

Author: empty
Version: 0.0.1
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from accounts.mixins.user_type_mixins import IsAdminViewMixin
from accounts.models import Account
from courses.models.course import Course
from departments.models.department import Department


class AdminDashboardHomeView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Admin Dashboard Home.

    Allowed HTTP verbs:
        - GET

    Restrictions:
        - LoginRequired
        - Admin user

    """

    def get(self, request, *args, **kwargs):
        accounts = Account.objects.actives()
        courses = Course.objects.all()
        departments = Department.objects.all()

        context = {
            "page_title": f"Admin Dashboard",
            "menu_section": "admin_dashboard",
            "menu_subsection": "admin_dashboard",
            "menu_action": "home",
            "accounts": accounts,
            "courses": courses,
            "departments": departments,
        }

        return render(request, "admin_dashboard/home/home.html", context)
