
from django.db import models


class TestDB(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    date_started = models.CharField(max_length=32, blank=True, null=True)