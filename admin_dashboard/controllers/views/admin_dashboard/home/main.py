"""
School Management System Project
Description for School Management System Project

Author: empty
Version: 0.0.1
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from academic_years.models import AcademicYear
from accounts.mixins.user_type_mixins import IsAdminViewMixin
from accounts.models import Account
from departments.models.department import Department
from subjects.models.subject import Subject


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
        subjects = Subject.objects.all()
        departments = Department.objects.all()
        academic_years = AcademicYear.objects.actives()

        context = {
            "page_title": f"Admin Dashboard",
            "menu_section": "admin_dashboard",
            "menu_subsection": "admin_dashboard",
            "menu_action": "home",
            "accounts": accounts,
            "subjects": subjects,
            "departments": departments,
            "academic_years": academic_years,
        }

        return render(request, "admin_dashboard/home/home.html", context)
