from faker import Faker
from django_test import TestCase


from subjects.models.subject_student.models import SubjectStudent as Master
from subjects.models.subject_student.factories import SubjectStudentFactory as MasterFactory

fake = Faker()


class SubjectStudentTest(TestCase):
    def test_create_subject_student(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )