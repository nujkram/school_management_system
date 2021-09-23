from faker import Faker
from django_test import TestCase


from subjects.models.subject.models import Subject as Master
from subjects.models.subject.factories import SubjectFactory as MasterFactory

fake = Faker()


class SubjectTest(TestCase):
    def test_create_subject(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )