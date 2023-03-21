from django import forms
from django.conf import settings
from django.db import models
from django.utils.module_loading import import_string

from .widgets import ImageInput


def default_upload_to(instance, filename):
    default_upload_to = getattr(settings, 'DEFAULT_UPLOAD_TO', None)
    if default_upload_to:
        return import_string(default_upload_to)(instance, filename)
    else:
        return f'uploads/db/{instance._meta.db_table}/{filename}'


class DefaultFileField(models.FileField):
    upload_to = default_upload_to


class DefaultImageField(models.ImageField):

    def __init__(self, upload_to=default_upload_to, **kwargs):
        kwargs.update(upload_to=upload_to)
        super().__init__(**kwargs)

    def formfield(self, **kwargs):

        class ImageField(forms.ImageField):
            widget = ImageInput

        defaults = {'form_class': ImageField}
        defaults.update(kwargs)
        return super().formfield(**defaults)
