from django.urls import path
from school_management_system.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicActivityListDetail,
    ApiPrivateActivityViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicActivityListDetail.as_view(URL_READ_ONLY),
        name='api_public_activity_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateActivityViewSet.as_view(URL_READ_ONLY),
        name='api_private_activity_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateActivityViewSet.as_view(URL_CREATE),
        name='api_private_activity_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateActivityViewSet.as_view(URL_UPDATE),
        name='api_private_activity_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateActivityViewSet.as_view(URL_DELETE),
        name='api_private_activity_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('activity/api/', include('activities.controllers.restapi.activity.urls'))
