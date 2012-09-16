# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ModelLog'
        db.create_table('kiwi_students_modellog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('target_instance', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('change_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('kiwi_students', ['ModelLog'])


    def backwards(self, orm):
        # Deleting model 'ModelLog'
        db.delete_table('kiwi_students_modellog')


    models = {
        'kiwi_students.groups': {
            'Meta': {'object_name': 'Groups'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'namegr': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'starosta': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'star'", 'null': 'True', 'to': "orm['kiwi_students.Students']"})
        },
        'kiwi_students.modellog': {
            'Meta': {'object_name': 'ModelLog'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'change_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'target_instance': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'kiwi_students.students': {
            'Meta': {'object_name': 'Students'},
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'st_group'", 'null': 'True', 'to': "orm['kiwi_students.Groups']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stud_ticket': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['kiwi_students']