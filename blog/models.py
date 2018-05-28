from django.db import models
import datetime
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')