from faker import Faker
from django_test import TestCase


from sections.models.section.models import Section as Master
from sections.models.section.factories import SectionFactory as MasterFactory

fake = Faker()


class SectionTest(TestCase):
    def test_create_section(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )