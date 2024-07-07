"""
    Regular Views supports here.
"""

from rest_framework.routers import DefaultRouter

from events.views import EventViews

router = DefaultRouter()

router.register(
    "events",
    EventViews,
)
