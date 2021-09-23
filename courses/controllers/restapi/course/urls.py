from django.urls import path
from school_management_system.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicCourseListDetail,
    ApiPrivateCourseViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicCourseListDetail.as_view(URL_READ_ONLY),
        name='api_public_course_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateCourseViewSet.as_view(URL_READ_ONLY),
        name='api_private_course_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateCourseViewSet.as_view(URL_CREATE),
        name='api_private_course_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateCourseViewSet.as_view(URL_UPDATE),
        name='api_private_course_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateCourseViewSet.as_view(URL_DELETE),
        name='api_private_course_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('course/api/', include('courses.controllers.restapi.course.urls'))
