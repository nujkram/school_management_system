import factory
from faker import Faker

from .models import Subject as Master

fake = Faker()


class SubjectFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
