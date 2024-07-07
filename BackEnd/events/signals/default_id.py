"""
    Implement function to generate id and return Id to models.
"""

from django.db.models.signals import pre_save
from django.dispatch import receiver
from events.utils import generate_id


def set_default_id(sender, instance, **kwargs):
    if not instance.id:
        instance.id = generate_id(instance)
