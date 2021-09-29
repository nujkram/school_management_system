from django.urls import path
from faculty_dashboard.controllers.views.faculty_dashboard.home import main as home_views

version = 'api/v1'

READ_ONLY = {
    'get': 'list'
}

urlpatterns = [
    path(
        '',
        home_views.FacultyDashboardHomeView.as_view(),
        name='faculty_dashboard_home_view'
    ),
]