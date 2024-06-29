"""
    Generate primary key for models.
"""

import uuid


def generate_id(instance: object, prefix: str = "id", length=8):
    uuid_code = str(uuid.uuid4())[:length]
    return f"{prefix}#{instance.__class__.__name__.lower()}#{uuid_code}"
