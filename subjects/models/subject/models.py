"""
School Management System
Subject 0.0.1
Subject models
Subject

Author: Christian
"""

import uuid as uuid
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from django.apps import apps
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .managers import SubjectManager as manager


class Subject(models.Model):
    # === Basic ===
    created = models.DateTimeField(null=False, auto_now_add=True)
    updated = models.DateTimeField(null=False, auto_now=True)

    # === Identifiers ===
    name = models.CharField(max_length=150)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, null=True, editable=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    # === Properties ===
    code = models.CharField(max_length=24, blank=True)

    # === State ===
    is_active = models.BooleanField(default=True)
    meta = models.JSONField(default=dict, blank=True, null=True)

    # === Relationship Fields ===
    department = models.ForeignKey(
        'departments.Department',
        null=True,
        db_index=False,
        on_delete=models.CASCADE,
        related_name='subjects_department'
    )
    grade_level = models.ForeignKey(
        'grade_levels.GradeLevel',
        null=True,
        db_index=False,
        on_delete=models.SET_NULL,
        related_name='subjects_year_level'
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        db_index=False,
        on_delete=models.SET_NULL,
        related_name='subjects_created_by_user'
    )
    last_updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        db_index=False,
        on_delete=models.SET_NULL,
        related_name='subjects_updated_by_user'
    )

    objects = manager()

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    ################################################################################
    # === Magic Methods ===
    ################################################################################
    def __str__(self):
        return self.name

        ################################################################################

    # === Model overrides ===
    ################################################################################
    def clean(self, *args, **kwargs):
        # add custom validation here
        super().clean()

    def save(self, *args, **kwargs):
        # self.full_clean()
        super().save(*args, **kwargs)

    ################################################################################
    # === Model-specific methods ===
    ################################################################################


################################################################################
# === Signals ===
################################################################################
@receiver(post_save, sender=Subject)
def scaffold_post_save(sender, instance=None, created=False, **kwargs):
    pass


@receiver(pre_save, sender=Subject)
def scaffold_pre_save(sender, instance=None, created=False, **kwargs):
    pass
