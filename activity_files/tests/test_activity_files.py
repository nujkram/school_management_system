from faker import Faker
from django_test import TestCase


from activity_files.models.activity_file.models import ActivityFile as Master
from activity_files.models.activity_file.factories import ActivityFileFactory as MasterFactory

fake = Faker()


class ActivityFileTest(TestCase):
    def test_create_activity_file(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )