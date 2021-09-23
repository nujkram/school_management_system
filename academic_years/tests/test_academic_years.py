from faker import Faker
from django_test import TestCase


from academic_years.models.academic_year.models import AcademicYear as Master
from academic_years.models.academic_year.factories import AcademicYearFactory as MasterFactory

fake = Faker()


class AcademicYearTest(TestCase):
    def test_create_academic_year(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )