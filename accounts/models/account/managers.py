from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.db import models
from django.utils.text import slugify
from .constants import USER, ADMIN, SUPERADMIN, FACULTY, STUDENT


class AccountQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(is_active=True).exclude(user_type=SUPERADMIN)

    def inactive(self):
        return self.filter(is_active=False)

    def admin(self):
        return self.filter(user_type=ADMIN)

    def faculty(self):
        return self.filter(user_type=FACULTY)

    def student(self):
        return self.filter(user_type=STUDENT)

    def latest(self):
        return self.order_by('-created')


class AccountManager(BaseUserManager):
    def get_queryset(self):
        return AccountQuerySet(self.model, using=self._db)

    def actives(self):
        return self.get_queryset().actives()

    def inactive(self):
        return self.get_queryset().inactive()

    def admins(self):
        return self.get_queryset().admin()

    def faculties(self):
        return self.get_queryset().faculty()

    def students(self):
        return self.get_queryset().student()

    def create_user(self, username=None, password=None, email=None, user_type=USER):
        """
        Create base user
        :param email:
        :param username:
        :param password:
        :param user_type:
        :param parent:
        :return: Account or False
        """
        if email:
            email_validator = EmailValidator()
            try:
                email_validator(email)
                email = self.normalize_email(email)
            except ValidationError:
                pass

        user = self.model(
            username=username,
            email=email,
            user_type=user_type
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email=None):
        user = self.create_user(
            username=username,
            password=password,
            email=email,
            user_type=SUPERADMIN
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
