# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.is_visible'
        db.add_column('posts_post', 'is_visible',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.is_visible'
        db.delete_column('posts_post', 'is_visible')


    models = {
        'posts.post': {
            'Meta': {'object_name': 'Post'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_favourite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['posts']