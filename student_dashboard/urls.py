from django.urls import path
from student_dashboard.controllers.views.student_dashboard.home import main as home_views

version = 'api/v1'

READ_ONLY = {
    'get': 'list'
}

urlpatterns = [
    path(
        '',
        home_views.StudentDashboardHomeView.as_view(),
        name='student_dashboard_home_view'
    ),
]

