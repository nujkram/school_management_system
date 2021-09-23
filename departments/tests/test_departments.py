from faker import Faker
from django_test import TestCase


from departments.models.department.models import Department as Master
from departments.models.department.factories import DepartmentFactory as MasterFactory

fake = Faker()


class DepartmentTest(TestCase):
    def test_create_department(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )