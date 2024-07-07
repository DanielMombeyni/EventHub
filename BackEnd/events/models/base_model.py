"""
    BaseModel just force other classes to use  some fields.
"""

from django.db import models
from events.utils import PrimaryKeyField


class BaseModel(models.Model):
    id = PrimaryKeyField(primary_key=True, unique=True, editable=False)

    class Meta:
        abstract = True
