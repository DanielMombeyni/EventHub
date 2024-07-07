"""
    Event Serializer.
"""

from rest_framework import serializers

from events.models import Event, Tag, Category
from .tag_serializer import TagSerializer
from .category_serializer import CategorySerializer


class EventSerializer(serializers.ModelSerializer):
    """Event Serializer."""

    tags = TagSerializer(many=True, required=False)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )
    # category_name = serializers.RelatedField(source="category", read_only=True)

    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "telegram_channel",
            "show_owner",
            "is_public",
            "date",
            "location",
            "description",
            "category",
            "category_id",
            "tags",
        )
        read_only_fields = ["id"]

    def _get_or_create_tags(self, tags: list[Tag], event: Event):
        """Handle getting or creating tags as needed."""
        for tag in tags:
            tag_object, created = Tag.objects.get_or_create(**tag)
            event.tags.add(tag_object)

    # def _get_category(self, category:Category, event: Event):

    def create(self, validated_data):
        """Create Event"""
        tags = validated_data.pop("tags", [])
        event = Event.objects.create(**validated_data)
        self._get_or_create_tags(tags, event)
        return event
