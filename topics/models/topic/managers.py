from django.db import models
from django.apps import apps


class TopicQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(is_active=True, deleted_at=None)

    def inactive(self):
        return self.filter(is_active=False)


class TopicManager(models.Manager):
    def get_queryset(self):
        return TopicQuerySet(self.model, using=self._db)
    
    def actives(self):
        return self.get_queryset().actives()

    def inactive(self):
        return self.get_queryset().inactive()
    
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)
