import factory
from faker import Faker

from .models import GradeLevel as Master

fake = Faker()


class GradeLevelFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
