import factory
from faker import Faker

from .models import ActivityFile as Master

fake = Faker()


class ActivityFileFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
