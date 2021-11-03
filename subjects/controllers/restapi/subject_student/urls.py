from django.urls import path
from school_management_system.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicSubjectStudentListDetail,
    ApiPrivateSubjectStudentViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicSubjectStudentListDetail.as_view(URL_READ_ONLY),
        name='api_public_subject_student_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateSubjectStudentViewSet.as_view(URL_READ_ONLY),
        name='api_private_subject_student_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateSubjectStudentViewSet.as_view(URL_CREATE),
        name='api_private_subject_student_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateSubjectStudentViewSet.as_view(URL_UPDATE),
        name='api_private_subject_student_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateSubjectStudentViewSet.as_view(URL_DELETE),
        name='api_private_subject_student_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('subject_student/api/', include('subjects.controllers.restapi.subject_student.urls'))
