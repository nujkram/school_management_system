from faker import Faker
from django_test import TestCase


from exercises.models.exercise.models import Exercise as Master
from exercises.models.exercise.factories import ExerciseFactory as MasterFactory

fake = Faker()


class ExerciseTest(TestCase):
    def test_create_exercise(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )