from django.urls import path

from admin_dashboard.controllers.views.admin_dashboard.academic_years import main as academic_years_views
from admin_dashboard.controllers.views.admin_dashboard.academic_year_subjects import main as academic_year_subjects_views
from admin_dashboard.controllers.views.admin_dashboard.accounts import main as accounts_views
from admin_dashboard.controllers.views.admin_dashboard.departments import main as departments_views
from admin_dashboard.controllers.views.admin_dashboard.home import main as home_views
from admin_dashboard.controllers.views.admin_dashboard.sections import main as sections_views
from admin_dashboard.controllers.views.admin_dashboard.subjects import main as subjects_views
from admin_dashboard.controllers.views.admin_dashboard.grade_levels import main as grade_levels_views

version = 'api/v1'

READ_ONLY = {
    'get': 'list'
}

urlpatterns = [
    path(
        '',
        home_views.AdminDashboardHomeView.as_view(),
        name='admin_dashboard_home_view'
    ),
]

urlpatterns += [
    path(
        'account/list',
        accounts_views.AdminDashboardAccountListView.as_view(),
        name='admin_dashboard_accounts_list'
    ),
    path(
        'account/<account>/detail',
        accounts_views.AdminDashboardAccountDetailView.as_view(),
        name='admin_dashboard_accounts_detail'
    ),
    path(
        'account/create',
        accounts_views.AdminDashboardAccountCreateView.as_view(),
        name='admin_dashboard_accounts_create'
    ),
    path(
        'account/<account>/update',
        accounts_views.AdminDashboardAccountUpdateView.as_view(),
        name='admin_dashboard_accounts_update'
    ),
    path(
        'account/<account>/delete',
        accounts_views.AdminDashboardAccountDeleteView.as_view(),
        name='admin_dashboard_accounts_delete'
    )
]

urlpatterns += [
    path(
        'academic_year/list',
        academic_years_views.AdminDashboardAcademicYearListView.as_view(),
        name='admin_dashboard_academic_years_list'
    ),
    path(
        'academic_year/<academic_year>/detail',
        academic_years_views.AdminDashboardAcademicYearDetailView.as_view(),
        name='admin_dashboard_academic_years_detail'
    ),
    path(
        'academic_year/create',
        academic_years_views.AdminDashboardAcademicYearCreateView.as_view(),
        name='admin_dashboard_academic_years_create'
    ),
    path(
        'academic_year/<academic_year>/update',
        academic_years_views.AdminDashboardAcademicYearUpdateView.as_view(),
        name='admin_dashboard_academic_years_update'
    ),
    path(
        'academic_year/<academic_year>/delete',
        academic_years_views.AdminDashboardAcademicYearDeleteView.as_view(),
        name='admin_dashboard_academic_years_delete'
    )
]

urlpatterns += [
    path(
        'academic_year_subject/<academic_year_subject>/list',
        academic_year_subjects_views.AdminDashboardAcademicYearSubjectListView.as_view(),
        name='admin_dashboard_academic_year_subjects_list'
    ),
    path(
        'academic_year_subject/<academic_year_subject>/detail',
        academic_year_subjects_views.AdminDashboardAcademicYearSubjectDetailView.as_view(),
        name='admin_dashboard_academic_year_subjects_detail'
    ),
    path(
        'academic_year_subject/create',
        academic_year_subjects_views.AdminDashboardAcademicYearSubjectCreateView.as_view(),
        name='admin_dashboard_academic_year_subjects_create'
    ),
    path(
        'academic_year_subject/<academic_year_subject>/update',
        academic_year_subjects_views.AdminDashboardAcademicYearSubjectUpdateView.as_view(),
        name='admin_dashboard_academic_year_subjects_update'
    ),
    path(
        'academic_year_subject/<academic_year_subject>/delete',
        academic_year_subjects_views.AdminDashboardAcademicYearSubjectDeleteView.as_view(),
        name='admin_dashboard_academic_year_subjects_delete'
    )
]

urlpatterns += [
    path(
        'department/list',
        departments_views.AdminDashboardDepartmentListView.as_view(),
        name='admin_dashboard_departments_list'
    ),
    path(
        'department/<department>/detail',
        departments_views.AdminDashboardDepartmentDetailView.as_view(),
        name='admin_dashboard_departments_detail'
    ),
    path(
        'department/create',
        departments_views.AdminDashboardDepartmentCreateView.as_view(),
        name='admin_dashboard_departments_create'
    ),
    path(
        'department/<department>/update',
        departments_views.AdminDashboardDepartmentUpdateView.as_view(),
        name='admin_dashboard_departments_update'
    ),
    path(
        'department/<department>/delete',
        departments_views.AdminDashboardDepartmentDeleteView.as_view(),
        name='admin_dashboard_departments_delete'
    )
]

urlpatterns += [
    path(
        'grade_level/list',
        grade_levels_views.AdminDashboardGradeLevelListView.as_view(),
        name='admin_dashboard_grade_levels_list'
    ),
    path(
        'grade_level/<grade_level>/detail',
        grade_levels_views.AdminDashboardGradeLevelDetailView.as_view(),
        name='admin_dashboard_grade_levels_detail'
    ),
    path(
        'grade_level/create',
        grade_levels_views.AdminDashboardGradeLevelCreateView.as_view(),
        name='admin_dashboard_grade_levels_create'
    ),
    path(
        'grade_level/<grade_level>/update',
        grade_levels_views.AdminDashboardGradeLevelUpdateView.as_view(),
        name='admin_dashboard_grade_levels_update'
    ),
    path(
        'grade_level/<grade_level>/delete',
        grade_levels_views.AdminDashboardGradeLevelDeleteView.as_view(),
        name='admin_dashboard_grade_levels_delete'
    )
]

urlpatterns += [
    path(
        'section/list',
        sections_views.AdminDashboardSectionListView.as_view(),
        name='admin_dashboard_sections_list'
    ),
    path(
        'section/<section>/detail',
        sections_views.AdminDashboardSectionDetailView.as_view(),
        name='admin_dashboard_sections_detail'
    ),
    path(
        'section/create',
        sections_views.AdminDashboardSectionCreateView.as_view(),
        name='admin_dashboard_sections_create'
    ),
    path(
        'section/<section>/update',
        sections_views.AdminDashboardSectionUpdateView.as_view(),
        name='admin_dashboard_sections_update'
    ),
    path(
        'section/<section>/delete',
        sections_views.AdminDashboardSectionDeleteView.as_view(),
        name='admin_dashboard_sections_delete'
    )
]

urlpatterns += [
    path(
        'subject/list',
        subjects_views.AdminDashboardSubjectListView.as_view(),
        name='admin_dashboard_subjects_list'
    ),
    path(
        'subject/<subject>/detail',
        subjects_views.AdminDashboardSubjectDetailView.as_view(),
        name='admin_dashboard_subjects_detail'
    ),
    path(
        'subject/create',
        subjects_views.AdminDashboardSubjectCreateView.as_view(),
        name='admin_dashboard_subjects_create'
    ),
    path(
        'subject/<subject>/update',
        subjects_views.AdminDashboardSubjectUpdateView.as_view(),
        name='admin_dashboard_subjects_update'
    ),
    path(
        'subject/<subject>/delete',
        subjects_views.AdminDashboardSubjectDeleteView.as_view(),
        name='admin_dashboard_subjects_delete'
    )
]