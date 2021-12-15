import factory
from faker import Faker

from .models import Exercise as Master

fake = Faker()


class ExerciseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
