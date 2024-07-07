"""
    Tags
"""

from django.db import models
from django.contrib.auth import get_user_model
from events.utils import image_file_path, generate_id
from events.models import BaseModel


class Tag(BaseModel):
    title = models.CharField(max_length=255, unique=True)
