"""
    Tags serializers
"""

from rest_framework import serializers
from events.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Tags serializers"""

    class Meta:
        model = Tag
        fields = ["id", "title"]
        read_only_fields = ["id"]
