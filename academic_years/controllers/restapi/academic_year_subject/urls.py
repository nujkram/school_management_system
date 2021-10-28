from django.urls import path
from school_management_system.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicAcademicYearSubjectListDetail,
    ApiPrivateAcademicYearSubjectViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicAcademicYearSubjectListDetail.as_view(URL_READ_ONLY),
        name='api_public_academic_year_subject_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateAcademicYearSubjectViewSet.as_view(URL_READ_ONLY),
        name='api_private_academic_year_subject_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateAcademicYearSubjectViewSet.as_view(URL_CREATE),
        name='api_private_academic_year_subject_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateAcademicYearSubjectViewSet.as_view(URL_UPDATE),
        name='api_private_academic_year_subject_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateAcademicYearSubjectViewSet.as_view(URL_DELETE),
        name='api_private_academic_year_subject_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('academic_year_subject/api/', include('academic_years.controllers.restapi.academic_year_subject.urls'))
