import factory
from faker import Faker

from .models import Department as Master

fake = Faker()


class DepartmentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
