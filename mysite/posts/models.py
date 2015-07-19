import datetime
from pyquery import PyQuery
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=400)
    pub_date = models.DateTimeField('date published', blank=True, null=True)
    is_favourite = models.BooleanField(
        default=False, verbose_name="Show on favourite posts page?")
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title if self.title != '' else self.text[:50]

    def save(self, *args, **kwargs):
        if not self.pub_date:
            self.pub_date = datetime.datetime.today()
        return super(Post, self).save(*args, **kwargs)

    def is_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # all stuff with html convertions is done here
    @property
    def processed_text(self):
        pq = PyQuery(self.text)
        if pq('iframe'):
            pq('iframe').wrap("<div class='responsive-video'>")
        if pq('img'):
            pq('img').addClass('img-responsive')
        return pq.outer_html()
