from django.urls import path
from school_management_system.urls import (
    URL_READ_ONLY,
    URL_DETAIL,
    URL_CREATE,
    URL_UPDATE,
    URL_DELETE
)

from .api import(
    ApiPublicExerciseListDetail,
    ApiPrivateExerciseViewSet
)

VERSION = 'v1'

urlpatterns = [
    # public
    path(
        f'{VERSION}/public/list',
        ApiPublicExerciseListDetail.as_view(URL_READ_ONLY),
        name='api_public_exercise_list_detail'
    ),

    # private
    path(
        f'{VERSION}/private/list',
        ApiPrivateExerciseViewSet.as_view(URL_READ_ONLY),
        name='api_private_exercise_list_detail'
    ),
    path(
        f'{VERSION}/private/create',
        ApiPrivateExerciseViewSet.as_view(URL_CREATE),
        name='api_private_exercise_create'
    ),
    path(
        f'{VERSION}/private/<pk>/update',
        ApiPrivateExerciseViewSet.as_view(URL_UPDATE),
        name='api_private_exercise_update'
    ),
    path(
        f'{VERSION}/private/<pk>/delete',
        ApiPrivateExerciseViewSet.as_view(URL_DELETE),
        name='api_private_exercise_delete'
    ),
]

"""
Add to urls.py urlpatterns:
    path('exercise/api/', include('exercises.controllers.restapi.exercise.urls'))
