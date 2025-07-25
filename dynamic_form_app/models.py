from django.db import models
from django.contrib.postgres.fields import JSONField


class FormData(models.Model):
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)