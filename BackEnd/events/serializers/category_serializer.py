"""
    Category serializers.
"""

from rest_framework import serializers
from events.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Category serializers"""

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "image",
        ]
        read_only_fields = ["id"]
