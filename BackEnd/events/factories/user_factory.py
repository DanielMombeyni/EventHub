import factory
from events.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "events.User"
        inline_args = ("username", "email")
        django_get_or_create = ("username", "email")

    username = "TestUser"
    image = factory.django.ImageField(color="blue")
    email = factory.LazyAttribute(lambda instance: f"{instance.username}@gmail.com")
    password = factory.django.Password("pw")

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)


class AdminFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        inline_args = ("username", "email")
        django_get_or_create = ("username", "email")

    username = "TestUserAdmin"
    email = factory.LazyAttribute(lambda instance: f"{instance.username}@gmail.com")
    password = factory.django.Password("pw")

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        manager = cls._get_manager(model_class)
        return manager.create_superuser(*args, **kwargs)
