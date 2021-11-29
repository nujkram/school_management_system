from django.urls import path
from student_dashboard.controllers.views.student_dashboard.home import main as home_views
from student_dashboard.controllers.views.student_dashboard.academic_years import main as academic_years_views
from student_dashboard.controllers.views.student_dashboard.academic_year_subjects import main as academic_year_subjects_views
from student_dashboard.controllers.views.student_dashboard.subjects import main as subjects_views
from student_dashboard.controllers.views.student_dashboard.topics import main as topics_views
from student_dashboard.controllers.views.student_dashboard.activities import main as activities_views

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

urlpatterns += [
    path(
        'academic_year_subject/<academic_year>/list',
        academic_year_subjects_views.StudentDashboardAcademicYearSubjectListView.as_view(),
        name='student_dashboard_academic_year_subjects_list'
    ),
    path(
        'academic_year_subject/<academic_year_subject>/detail',
        academic_year_subjects_views.StudentDashboardAcademicYearSubjectDetailView.as_view(),
        name='student_dashboard_academic_year_subjects_detail'
    ),
    path(
        'academic_year_subject/create',
        academic_year_subjects_views.StudentDashboardAcademicYearSubjectCreateView.as_view(),
        name='student_dashboard_academic_year_subjects_create'
    ),
    path(
        'academic_year_subject/<academic_year_subject>/update',
        academic_year_subjects_views.StudentDashboardAcademicYearSubjectUpdateView.as_view(),
        name='student_dashboard_academic_year_subjects_update'
    ),
    path(
        'academic_year_subject/<academic_year_subject>/delete',
        academic_year_subjects_views.StudentDashboardAcademicYearSubjectDeleteView.as_view(),
        name='student_dashboard_academic_year_subjects_delete'
    )
]

urlpatterns += [
    path(
        'subject/list',
        subjects_views.StudentDashboardSubjectListView.as_view(),
        name='student_dashboard_subjects_list'
    ),
    path(
        'subject/<subject>/detail',
        subjects_views.StudentDashboardSubjectDetailView.as_view(),
        name='student_dashboard_subjects_detail'
    ),
    path(
        'subject/create',
        subjects_views.StudentDashboardSubjectCreateView.as_view(),
        name='student_dashboard_subjects_create'
    ),
    path(
        'subject/<subject>/update',
        subjects_views.StudentDashboardSubjectUpdateView.as_view(),
        name='student_dashboard_subjects_update'
    ),
    path(
        'subject/<subject>/delete',
        subjects_views.StudentDashboardSubjectDeleteView.as_view(),
        name='student_dashboard_subjects_delete'
    )
]

urlpatterns += [
    path(
        'topic/<academic_year_subject>/list',
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

urlpatterns += [
    path(
        'activity/list',
        activities_views.StudentDashboardActivityListView.as_view(),
        name='student_dashboard_activities_list'
    ),
    path(
        'activity/<activity>/detail',
        activities_views.StudentDashboardActivityDetailView.as_view(),
        name='student_dashboard_activities_detail'
    ),
    path(
        'activity/create',
        activities_views.StudentDashboardActivityCreateView.as_view(),
        name='student_dashboard_activities_create'
    ),
    path(
        'activity/<activity>/update',
        activities_views.StudentDashboardActivityUpdateView.as_view(),
        name='student_dashboard_activities_update'
    ),
    path(
        'activity/<activity>/delete',
        activities_views.StudentDashboardActivityDeleteView.as_view(),
        name='student_dashboard_activities_delete'
    )
]