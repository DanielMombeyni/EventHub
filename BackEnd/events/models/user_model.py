"""
    User Model for System.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db.models.signals import pre_save
from django.dispatch import receiver

from events.utils import image_file_path, generate_id


class UserManager(BaseUserManager):
    """Manager for user"""

    def create_user(
        self, username: str, email: str, password: str, **extra_fields: dict
    ):
        """Create, save and return a new user"""
        if not email:
            raise ValueError("User must have an email address.")
        if not username:
            raise ValueError("User must have an UserName address.")
        email = self.normalize_email(email)
        if self.model.objects.filter(email=email).exists():
            raise ValueError("Email is already taken.")
        user = self.model(
            email=email,
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username: str, email: str, password: str):
        """Create, save and return a new superuser"""
        if self.model.objects.filter(email=email).exists():
            raise ValueError("Email is already taken.")

        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """implementation User for the system."""

    id = models.CharField(primary_key=True, unique=True, editable=False)
    image = models.ImageField(null=True, upload_to=image_file_path)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=12, unique=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return self.id


@receiver(pre_save, sender=User)
def set_default_id(sender, instance, **kwargs):
    if not instance.id:
        instance.id = generate_id(instance)
