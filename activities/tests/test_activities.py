from faker import Faker
from django_test import TestCase


from activities.models.activity.models import Activity as Master
from activities.models.activity.factories import ActivityFactory as MasterFactory

fake = Faker()


class ActivityTest(TestCase):
    def test_create_activity(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )