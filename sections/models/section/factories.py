import factory
from faker import Faker

from .models import Section as Master

fake = Faker()


class SectionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
