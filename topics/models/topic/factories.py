import factory
from faker import Faker

from .models import Topic as Master

fake = Faker()


class TopicFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
