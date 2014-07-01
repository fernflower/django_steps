from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField('birthday')
    info = models.TextField(max_length=400)

    def __str__(self):
        return self.name
