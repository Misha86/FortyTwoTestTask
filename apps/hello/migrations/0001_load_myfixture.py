# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."


    def backwards(self, orm):
        "Write your backwards methods here."
        from django.core.management import call_command
        call_command("loaddata", "person_data.json")

    models = {
        u'hello.contacts': {
            'Meta': {'ordering': "['person']", 'object_name': 'Contacts'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'person': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'contacts'", 'unique': 'True', 'to': u"orm['hello.Person']"}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hello.person': {
            'Meta': {'ordering': "['name']", 'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {'unique': 'True', 'max_length': "'1000'"}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['hello']
    symmetrical = True
