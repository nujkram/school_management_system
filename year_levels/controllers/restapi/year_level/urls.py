from django.urls import path
from school_management_system.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicYearLevelListDetail,
    ApiPrivateYearLevelViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicYearLevelListDetail.as_view(URL_READ_ONLY),
        name='api_public_year_level_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateYearLevelViewSet.as_view(URL_READ_ONLY),
        name='api_private_year_level_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateYearLevelViewSet.as_view(URL_CREATE),
        name='api_private_year_level_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateYearLevelViewSet.as_view(URL_UPDATE),
        name='api_private_year_level_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateYearLevelViewSet.as_view(URL_DELETE),
        name='api_private_year_level_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('year_level/api/', include('year_levels.controllers.restapi.year_level.urls'))
