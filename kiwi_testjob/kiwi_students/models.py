from django.db import models
from django.db.models.signals import post_save, post_delete
from signals import ModelChangeLog
from datetime import time


class Groups(models.Model):
     namegr = models.CharField(max_length=30, verbose_name='Название группы')
     starosta = models.ForeignKey('Students', blank=True, null=True,
                                  related_name='star', verbose_name='Староста')

     def __unicode__(self):
          return self.namegr

class Students(models.Model):
     fio = models.CharField(max_length=75, verbose_name='ФИО')
     birth_date = models.DateField(auto_now=False, auto_now_add=False,
                                   verbose_name='Дата рождения')
     stud_ticket = models.CharField(max_length=10, verbose_name='Студбилет')
     group = models.ForeignKey(Groups, blank=True, null=True,
                               related_name='st_group', verbose_name='Группа')

     def __unicode__(self):
          return self.fio


class ModelLog(models.Model):
    model = models.CharField(max_length=30)
    action = models.CharField(max_length=15)
    target_instance = models.CharField(max_length=255, blank=True, null=True)
    change_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return "%s %s %s %s" % (self.model, self.target_instance,
                                self.action, self.change_timestamp)


post_save.connect(ModelChangeLog,
                  dispatch_uid="%s%s" % (time.second, time.microsecond))
post_delete.connect(ModelChangeLog,
                    dispatch_uid="%s%s" % (time.second, time.microsecond))
