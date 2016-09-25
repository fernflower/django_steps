import datetime

from adminfiles import utils
from django.db import models
from django.utils import timezone
from pyquery import PyQuery

import django_markdown.models
import markdown

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^django_markdown\.models\.MarkdownField"])


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = django_markdown.models.MarkdownField()
    summary = django_markdown.models.MarkdownField(default='', blank=True,
                                                   null=True)
    pub_date = models.DateTimeField('date published', blank=True, null=True)
    is_favourite = models.BooleanField(
        default=False, verbose_name="Show on favourite posts page?")
    is_visible = models.BooleanField(default=True)

    def __unicode__(self):
        unic_title = self.title if self.title != '' else self.text[:50]
        return unicode(unic_title)

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
        markdowned = markdown.markdown(utils.render_uploads(self.text))
        pq = PyQuery(markdowned)
        if pq('iframe'):
            pq('iframe').wrap("<div class='responsive-video'>")
        if pq('img'):
            pq('img').addClass('img-responsive')
        return pq.outer_html()
