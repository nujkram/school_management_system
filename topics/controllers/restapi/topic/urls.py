from django.urls import path
from school_management_system.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicTopicListDetail,
    ApiPrivateTopicViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicTopicListDetail.as_view(URL_READ_ONLY),
        name='api_public_topic_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateTopicViewSet.as_view(URL_READ_ONLY),
        name='api_private_topic_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateTopicViewSet.as_view(URL_CREATE),
        name='api_private_topic_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateTopicViewSet.as_view(URL_UPDATE),
        name='api_private_topic_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateTopicViewSet.as_view(URL_DELETE),
        name='api_private_topic_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('topic/api/', include('topics.controllers.restapi.topic.urls'))
