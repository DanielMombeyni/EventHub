"""
    Generate primary key for models.
"""

import uuid


def generate_id(instance: object, length=8, *args, **kwargs):
    uuid_code = str(uuid.uuid4())[:length]
    return f"{instance.__class__.__name__.lower()}#{uuid_code}"
