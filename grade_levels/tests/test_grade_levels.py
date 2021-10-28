from faker import Faker
from django_test import TestCase


from grade_levels.models.grade_level.models import GradeLevel as Master
from grade_levels.models.grade_level.factories import GradeLevelFactory as MasterFactory

fake = Faker()


class GradeLevelTest(TestCase):
    def test_create_grade_level(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )