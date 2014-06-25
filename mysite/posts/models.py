import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.text

    def is_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
