import factory
from faker import Faker

from .models import YearLevel as Master

fake = Faker()


class YearLevelFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
