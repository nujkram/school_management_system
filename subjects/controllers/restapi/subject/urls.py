from django.urls import path
from school_management_system.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicSubjectListDetail,
    ApiPrivateSubjectViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicSubjectListDetail.as_view(URL_READ_ONLY),
        name='api_public_subject_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateSubjectViewSet.as_view(URL_READ_ONLY),
        name='api_private_subject_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateSubjectViewSet.as_view(URL_CREATE),
        name='api_private_subject_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateSubjectViewSet.as_view(URL_UPDATE),
        name='api_private_subject_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateSubjectViewSet.as_view(URL_DELETE),
        name='api_private_subject_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('subject/api/', include('subjects.controllers.restapi.subject.urls'))
