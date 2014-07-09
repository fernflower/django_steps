from django.db import models
from django.conf import settings


class Member(models.Model):
    name = models.CharField(max_length=100)
    # if alias is set than member can be addressed no only as about/member_id,
    # but also about/member_alias
    alias = models.CharField(max_length=10, choices=zip(settings.MEMBER_ALIASES,
                                                        settings.MEMBER_ALIASES))
    birthday = models.DateField('birthday', blank=True, null=True)
    info = models.TextField(max_length=400)

    def __str__(self):
        return self.name
