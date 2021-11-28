from faker import Faker
from django_test import TestCase


from topics.models.topic.models import Topic as Master
from topics.models.topic.factories import TopicFactory as MasterFactory

fake = Faker()


class TopicTest(TestCase):
    def test_create_topic(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )