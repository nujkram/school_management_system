from faker import Faker
from django_test import TestCase


from courses.models.course.models import Course as Master
from courses.models.course.factories import CourseFactory as MasterFactory

fake = Faker()


class CourseTest(TestCase):
    def test_create_course(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )