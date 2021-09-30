from django.urls import path
from school_management_system.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicSectionListDetail,
    ApiPrivateSectionViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicSectionListDetail.as_view(URL_READ_ONLY),
        name='api_public_section_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateSectionViewSet.as_view(URL_READ_ONLY),
        name='api_private_section_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateSectionViewSet.as_view(URL_CREATE),
        name='api_private_section_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateSectionViewSet.as_view(URL_UPDATE),
        name='api_private_section_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateSectionViewSet.as_view(URL_DELETE),
        name='api_private_section_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('section/api/', include('sections.controllers.restapi.section.urls'))
