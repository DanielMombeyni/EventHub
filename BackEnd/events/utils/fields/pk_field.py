from django.db import models
from events.utils import generate_id


class PrimaryKeyField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["primary_key"] = True
        kwargs["editable"] = False
        kwargs["unique"] = True
        super().__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name, private_only=False):
        self._instance_name = cls.__name__.lower()
        super().contribute_to_class(cls, name, private_only)
        setattr(cls, name, self)

    def pre_save(self, model_instance, add):
        value = super().pre_save(model_instance, add)
        if not value:
            value = generate_id(instance=self._instance_name)
            setattr(model_instance, self.attname, value)
        return value
