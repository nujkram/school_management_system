import factory
from faker import Faker

from .models import Course as Master

fake = Faker()


class CourseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
