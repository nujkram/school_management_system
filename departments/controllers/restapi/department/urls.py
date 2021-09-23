from django.urls import path
from school_management_system.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicDepartmentListDetail,
    ApiPrivateDepartmentViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicDepartmentListDetail.as_view(URL_READ_ONLY),
        name='api_public_department_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateDepartmentViewSet.as_view(URL_READ_ONLY),
        name='api_private_department_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateDepartmentViewSet.as_view(URL_CREATE),
        name='api_private_department_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateDepartmentViewSet.as_view(URL_UPDATE),
        name='api_private_department_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateDepartmentViewSet.as_view(URL_DELETE),
        name='api_private_department_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('department/api/', include('departments.controllers.restapi.department.urls'))
