"""
School Management System
Academic Year 0.0.1
Academic Year Subject models
Academic Year Subject

Author: Empty
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

from accounts.models.account.constants import FACULTY
from .managers import AcademicYearSubjectManager as manager


class AcademicYearSubject(models.Model):
    # === Basic ===
    created = models.DateTimeField(null=False, auto_now_add=True)
    updated = models.DateTimeField(null=False, auto_now=True)

    # === Identifiers ===

    # === Properties ===
    

    # === State ===
    is_active = models.BooleanField(default=True)
    meta = models.JSONField(default=dict, blank=True, null=True)

    # === Relationship Fields ===
    academic_year = models.ForeignKey(
        'academic_years.AcademicYear',
        null=False,
        db_index=False,
        on_delete=models.CASCADE,
        related_name='academic_year_subjects'
    )
    grade_level = models.ForeignKey(
        'grade_levels.GradeLevel',
        null=False,
        db_index=False,
        on_delete=models.CASCADE,
        related_name='academic_year_grade_levels_data'
    )
    subject = models.ForeignKey(
        'subjects.Subject',
        null=False,
        db_index=False,
        on_delete=models.CASCADE,
        related_name='academic_year_subjects_data'
    )
    faculty = models.ForeignKey(
        'accounts.Account',
        null=False,
        db_index=False,
        on_delete=models.CASCADE,
        limit_choices_to={'user_type': FACULTY},
        related_name='academic_year_subjects_data'
    )
    section = models.ForeignKey(
        'sections.Section',
        null=False,
        db_index=False,
        on_delete=models.CASCADE,
        related_name='academic_year_sections_data'
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        db_index=False,
        on_delete=models.SET_NULL,
        related_name='academic_year_subjects_created_by_user'
    )
    last_updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        db_index=False,
        on_delete=models.SET_NULL,
        related_name='academic_year_subjects_updated_by_user'
    )

    objects = manager()

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Academic Year Subject'
        verbose_name_plural = 'Academic Year Subjects'
    
    ################################################################################
    # === Magic Methods ===
    ################################################################################
    def __str__(self):
        return self.subject.code + " " + self.academic_year.name

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
@receiver(post_save, sender=AcademicYearSubject)
def scaffold_post_save(sender, instance=None, created=False, **kwargs):
    pass


@receiver(pre_save, sender=AcademicYearSubject)
def scaffold_pre_save(sender, instance=None, created=False, **kwargs):
    pass
