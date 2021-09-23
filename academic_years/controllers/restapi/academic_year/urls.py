from django.urls import path
from school_management_system.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicAcademicYearListDetail,
    ApiPrivateAcademicYearViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicAcademicYearListDetail.as_view(URL_READ_ONLY),
        name='api_public_academic_year_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateAcademicYearViewSet.as_view(URL_READ_ONLY),
        name='api_private_academic_year_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateAcademicYearViewSet.as_view(URL_CREATE),
        name='api_private_academic_year_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateAcademicYearViewSet.as_view(URL_UPDATE),
        name='api_private_academic_year_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateAcademicYearViewSet.as_view(URL_DELETE),
        name='api_private_academic_year_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('academic_year/api/', include('academic_years.controllers.restapi.academic_year.urls'))
