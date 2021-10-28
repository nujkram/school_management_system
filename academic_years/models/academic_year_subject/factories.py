import factory
from faker import Faker

from .models import AcademicYearSubject as Master

fake = Faker()


class AcademicYearSubjectFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
