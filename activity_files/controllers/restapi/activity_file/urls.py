from django.urls import path
from school_management_system.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicActivityFileListDetail,
    ApiPrivateActivityFileViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicActivityFileListDetail.as_view(URL_READ_ONLY),
        name='api_public_activity_file_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateActivityFileViewSet.as_view(URL_READ_ONLY),
        name='api_private_activity_file_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateActivityFileViewSet.as_view(URL_CREATE),
        name='api_private_activity_file_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateActivityFileViewSet.as_view(URL_UPDATE),
        name='api_private_activity_file_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateActivityFileViewSet.as_view(URL_DELETE),
        name='api_private_activity_file_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('activity_file/api/', include('activity_files.controllers.restapi.activity_file.urls'))
