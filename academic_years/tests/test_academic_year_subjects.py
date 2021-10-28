from faker import Faker
from django_test import TestCase


from academic_years.models.academic_year_subject.models import AcademicYearSubject as Master
from academic_years.models.academic_year_subject.factories import AcademicYearSubjectFactory as MasterFactory

fake = Faker()


class AcademicYearSubjectTest(TestCase):
    def test_create_academic_year_subject(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )