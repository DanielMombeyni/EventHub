"""
    Event model.
"""

from django.db import models
from django.contrib.auth import get_user_model
from events.utils import image_file_path
from events.models import BaseModel
from .tags_model import Tag

User = get_user_model()


class Category(BaseModel):
    id = models.CharField(primary_key=True, unique=True, editable=False)
    image = models.ImageField(null=True, upload_to=image_file_path)
    title = models.CharField(max_length=255, blank=False, null=False)


class Event(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="events"
    )
    is_public = models.BooleanField(default=True)
    show_owner = models.BooleanField(default=True)
    telegram_channel = models.CharField(max_length=255, blank=False, null=False)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    # members = models.ManyToManyField(User, related_name="joined_events", blank=True)
    tags = models.ManyToManyField(Tag, related_name="events", blank=True)

    def __str__(self) -> str:
        return f"{self.title}"
