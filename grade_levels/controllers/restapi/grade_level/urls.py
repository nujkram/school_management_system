from django.urls import path
from school_management_system.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicGradeLevelListDetail,
    ApiPrivateGradeLevelViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicGradeLevelListDetail.as_view(URL_READ_ONLY),
        name='api_public_grade_level_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateGradeLevelViewSet.as_view(URL_READ_ONLY),
        name='api_private_grade_level_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateGradeLevelViewSet.as_view(URL_CREATE),
        name='api_private_grade_level_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateGradeLevelViewSet.as_view(URL_UPDATE),
        name='api_private_grade_level_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateGradeLevelViewSet.as_view(URL_DELETE),
        name='api_private_grade_level_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('grade_level/api/', include('grade_levels.controllers.restapi.grade_level.urls'))
