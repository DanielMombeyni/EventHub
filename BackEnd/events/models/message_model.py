"""
    Message
"""

from django.db import models
from django.contrib.auth import get_user_model

# from events.utils import image_file_path, generate_id
from events.models import BaseModel, Event

User = get_user_model()


class Message(BaseModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} in {self.event.title}"
