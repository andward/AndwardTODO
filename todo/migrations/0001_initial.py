# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Task'
        db.create_table(u'todo_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('expiry', self.gf('django.db.models.fields.DateTimeField')()),
            ('expiry_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'todo', ['Task'])

        # Adding model 'Comment'
        db.create_table(u'todo_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mark', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'todo', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Task'
        db.delete_table(u'todo_task')

        # Deleting model 'Comment'
        db.delete_table(u'todo_comment')


    models = {
        u'todo.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mark': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'todo.task': {
            'Meta': {'object_name': 'Task'},
            'expiry': ('django.db.models.fields.DateTimeField', [], {}),
            'expiry_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['todo']