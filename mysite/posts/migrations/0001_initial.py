# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('text', django_markdown.models.MarkdownField()),
                ('summary', django_markdown.models.MarkdownField(default=b'', null=True, blank=True)),
                ('pub_date', models.DateTimeField(null=True, verbose_name=b'date published', blank=True)),
                ('is_favourite', models.BooleanField(default=False, verbose_name=b'Show on favourite posts page?')),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
    ]
