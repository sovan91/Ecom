from django.db import models
from datetime import *


class Event(models.Model):
    name = models.CharField('Event Name', max_length=200)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=130)
    manager = models.CharField(max_length=120)
    description = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name
