from faker import Faker
from django_test import TestCase


from year_levels.models.year_level.models import YearLevel as Master
from year_levels.models.year_level.factories import YearLevelFactory as MasterFactory

fake = Faker()


class YearLevelTest(TestCase):
    def test_create_year_level(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )