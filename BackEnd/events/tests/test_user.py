"""
    Test User Model (CRUD).
"""

from django.contrib.auth.hashers import check_password
from django.test import TestCase
from events.models import User
from events.factories import (
    UserFactory,
    AdminFactory,
)

import os
import tempfile
from datetime import datetime


class TestUserModel(TestCase):
    def setUp(self) -> None:
        self.payload = {
            "username": "TestUser",
        }
        self.user = UserFactory(**self.payload)
        self.user_admin = AdminFactory()

    def test_create_user(self):
        """Test Create Normal User."""

        self.assertEqual(self.user.username, self.payload.get("username"))
        self.assertEqual(self.user.is_active, True)
        self.assertFalse(self.user.is_staff, False)

        self.assertTrue(
            User.objects.filter(username=self.payload.get("username")).exists()
        )
