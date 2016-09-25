# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.summary'
        db.add_column(u'posts_post', 'summary',
                      self.gf('django_markdown.models.MarkdownField')(default=''),
                      keep_default=False)


        # Changing field 'Post.text'
        db.alter_column(u'posts_post', 'text', self.gf('django_markdown.models.MarkdownField')())

    def backwards(self, orm):
        # Deleting field 'Post.summary'
        db.delete_column(u'posts_post', 'summary')


        # Changing field 'Post.text'
        db.alter_column(u'posts_post', 'text', self.gf('django.db.models.fields.TextField')(max_length=400))

    models = {
        u'posts.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_favourite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'summary': ('django_markdown.models.MarkdownField', [], {'default': "''"}),
            'text': ('django_markdown.models.MarkdownField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['posts']