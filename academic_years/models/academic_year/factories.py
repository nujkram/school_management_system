import factory
from faker import Faker

from .models import AcademicYear as Master

fake = Faker()


class AcademicYearFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
