import factory
from faker import Faker

from .models import Activity as Master

fake = Faker()


class ActivityFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
