"""
    Generates a unique file path for an image file associated with a specific instance of a class.
"""

import os
from uuid import uuid4


def image_file_path(instance: object, file_name):
    """Generate file path for new Classes image."""
    ext = os.path.splitext(file_name)[1]
    file_name = f"{uuid4()}{ext}"
    return os.path.join("uploads", f"{instance.__class__.__name__.lower()}", file_name)
