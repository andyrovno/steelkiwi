# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Groups'
        db.create_table('kiwi_students_groups', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('namegr', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('starosta', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='star', null=True, to=orm['kiwi_students.Students'])),
        ))
        db.send_create_signal('kiwi_students', ['Groups'])

        # Adding model 'Students'
        db.create_table('kiwi_students_students', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fio', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('stud_ticket', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='st_group', null=True, to=orm['kiwi_students.Groups'])),
        ))
        db.send_create_signal('kiwi_students', ['Students'])


    def backwards(self, orm):
        # Deleting model 'Groups'
        db.delete_table('kiwi_students_groups')

        # Deleting model 'Students'
        db.delete_table('kiwi_students_students')


    models = {
        'kiwi_students.groups': {
            'Meta': {'object_name': 'Groups'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'namegr': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'starosta': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'star'", 'null': 'True', 'to': "orm['kiwi_students.Students']"})
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