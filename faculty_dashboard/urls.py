from django.urls import path
from faculty_dashboard.controllers.views.faculty_dashboard.home import main as home_views
from faculty_dashboard.controllers.views.faculty_dashboard.academic_years import main as academic_years_views
from faculty_dashboard.controllers.views.faculty_dashboard.academic_year_subjects import main as academic_year_subjects_views
from faculty_dashboard.controllers.views.faculty_dashboard.subjects import main as subjects_views
from faculty_dashboard.controllers.views.faculty_dashboard.subject_students import main as subject_students_views
from faculty_dashboard.controllers.views.faculty_dashboard.topics import main as topics_views
from faculty_dashboard.controllers.views.faculty_dashboard.activities import main as activities_views
from faculty_dashboard.controllers.views.faculty_dashboard.exercises import main as exercises_views
from faculty_dashboard.controllers.views.faculty_dashboard.activity_files import main as activity_files_views

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

urlpatterns += [
    path(
        'academic_year/list',
        academic_years_views.FacultyDashboardAcademicYearListView.as_view(),
        name='faculty_dashboard_academic_years_list'
    ),
    path(
        'academic_year/<academic_year>/detail',
        academic_years_views.FacultyDashboardAcademicYearDetailView.as_view(),
        name='faculty_dashboard_academic_years_detail'
    ),
    path(
        'academic_year/create',
        academic_years_views.FacultyDashboardAcademicYearCreateView.as_view(),
        name='faculty_dashboard_academic_years_create'
    ),
    path(
        'academic_year/<academic_year>/update',
        academic_years_views.FacultyDashboardAcademicYearUpdateView.as_view(),
        name='faculty_dashboard_academic_years_update'
    ),
    path(
        'academic_year/<academic_year>/delete',
        academic_years_views.FacultyDashboardAcademicYearDeleteView.as_view(),
        name='faculty_dashboard_academic_years_delete'
    )
]

urlpatterns += [
    path(
        'academic_year_subject/<academic_year>/list',
        academic_year_subjects_views.FacultyDashboardAcademicYearSubjectListView.as_view(),
        name='faculty_dashboard_academic_year_subjects_list'
    ),
    path(
        'academic_year_subject/<academic_year_subject>/detail',
        academic_year_subjects_views.FacultyDashboardAcademicYearSubjectDetailView.as_view(),
        name='faculty_dashboard_academic_year_subjects_detail'
    ),
    path(
        'academic_year_subject/create',
        academic_year_subjects_views.FacultyDashboardAcademicYearSubjectCreateView.as_view(),
        name='faculty_dashboard_academic_year_subjects_create'
    ),
    path(
        'academic_year_subject/<academic_year_subject>/update',
        academic_year_subjects_views.FacultyDashboardAcademicYearSubjectUpdateView.as_view(),
        name='faculty_dashboard_academic_year_subjects_update'
    ),
    path(
        'academic_year_subject/<academic_year_subject>/delete',
        academic_year_subjects_views.FacultyDashboardAcademicYearSubjectDeleteView.as_view(),
        name='faculty_dashboard_academic_year_subjects_delete'
    )
]

urlpatterns += [
    path(
        'subject/list',
        subjects_views.FacultyDashboardSubjectListView.as_view(),
        name='faculty_dashboard_subjects_list'
    ),
    path(
        'subject/<subject>/detail',
        subjects_views.FacultyDashboardSubjectDetailView.as_view(),
        name='faculty_dashboard_subjects_detail'
    ),
    path(
        'subject/create',
        subjects_views.FacultyDashboardSubjectCreateView.as_view(),
        name='faculty_dashboard_subjects_create'
    ),
    path(
        'subject/<subject>/update',
        subjects_views.FacultyDashboardSubjectUpdateView.as_view(),
        name='faculty_dashboard_subjects_update'
    ),
    path(
        'subject/<subject>/delete',
        subjects_views.FacultyDashboardSubjectDeleteView.as_view(),
        name='faculty_dashboard_subjects_delete'
    )
]

urlpatterns += [
    path(
        'subject_student/<academic_year_subject>/list',
        subject_students_views.FacultyDashboardSubjectStudentListView.as_view(),
        name='faculty_dashboard_subject_students_list'
    ),
    path(
        'subject_student/<subject_student>/detail',
        subject_students_views.FacultyDashboardSubjectStudentDetailView.as_view(),
        name='faculty_dashboard_subject_students_detail'
    ),
    path(
        'subject_student/create',
        subject_students_views.FacultyDashboardSubjectStudentCreateView.as_view(),
        name='faculty_dashboard_subject_students_create'
    ),
    path(
        'subject_student/<subject_student>/update',
        subject_students_views.FacultyDashboardSubjectStudentUpdateView.as_view(),
        name='faculty_dashboard_subject_students_update'
    ),
    path(
        'subject_student/<subject_student>/delete',
        subject_students_views.FacultyDashboardSubjectStudentDeleteView.as_view(),
        name='faculty_dashboard_subject_students_delete'
    )
]

urlpatterns += [
    path(
        'topic/<academic_year_subject>/list',
        topics_views.FacultyDashboardTopicListView.as_view(),
        name='faculty_dashboard_topics_list'
    ),
    path(
        'topic/<topic>/detail',
        topics_views.FacultyDashboardTopicDetailView.as_view(),
        name='faculty_dashboard_topics_detail'
    ),
    path(
        'topic/create',
        topics_views.FacultyDashboardTopicCreateView.as_view(),
        name='faculty_dashboard_topics_create'
    ),
    path(
        'topic/<topic>/update',
        topics_views.FacultyDashboardTopicUpdateView.as_view(),
        name='faculty_dashboard_topics_update'
    ),
    path(
        'topic/<topic>/delete',
        topics_views.FacultyDashboardTopicDeleteView.as_view(),
        name='faculty_dashboard_topics_delete'
    )
]

urlpatterns += [
    path(
        'activity/list',
        activities_views.FacultyDashboardActivityListView.as_view(),
        name='faculty_dashboard_activities_list'
    ),
    path(
        'activity/<activity>/detail',
        activities_views.FacultyDashboardActivityDetailView.as_view(),
        name='faculty_dashboard_activities_detail'
    ),
    path(
        'activity/create',
        activities_views.FacultyDashboardActivityCreateView.as_view(),
        name='faculty_dashboard_activities_create'
    ),
    path(
        'activity/<activity>/update',
        activities_views.FacultyDashboardActivityUpdateView.as_view(),
        name='faculty_dashboard_activities_update'
    ),
    path(
        'activity/<activity>/delete',
        activities_views.FacultyDashboardActivityDeleteView.as_view(),
        name='faculty_dashboard_activities_delete'
    )
]

urlpatterns += [
    path(
        'exercise/<activity>/list',
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

urlpatterns += [
    path(
        'activity_file/list',
        activity_files_views.FacultyDashboardActivityFileListView.as_view(),
        name='faculty_dashboard_activity_files_list'
    ),
    path(
        'activity_file/<activity_file>/detail',
        activity_files_views.FacultyDashboardActivityFileDetailView.as_view(),
        name='faculty_dashboard_activity_files_detail'
    ),
    path(
        'activity_file/create',
        activity_files_views.FacultyDashboardActivityFileCreateView.as_view(),
        name='faculty_dashboard_activity_files_create'
    ),
    path(
        'activity_file/<activity_file>/update',
        activity_files_views.FacultyDashboardActivityFileUpdateView.as_view(),
        name='faculty_dashboard_activity_files_update'
    ),
    path(
        'activity_file/<activity_file>/delete',
        activity_files_views.FacultyDashboardActivityFileDeleteView.as_view(),
        name='faculty_dashboard_activity_files_delete'
    )
]
