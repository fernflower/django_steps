# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table('posts_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=400)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('is_favourite', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('posts', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table('posts_post')


    models = {
        'posts.post': {
            'Meta': {'object_name': 'Post'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_favourite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['posts']