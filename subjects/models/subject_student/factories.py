import factory
from faker import Faker

from .models import SubjectStudent as Master

fake = Faker()


class SubjectStudentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
