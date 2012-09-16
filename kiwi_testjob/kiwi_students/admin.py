from django.contrib import admin
from kiwi_testjob.kiwi_students.models import Groups, Students, ModelLog


class StudInline(admin.TabularInline):
     model = Students
     extra = 1


class GroupsAdmin(admin.ModelAdmin):
     list_display = ('namegr', 'starosta',)
     search_fields = ['namegr', 'star']
     inlines = (StudInline,)


class StudentsAdmin(admin.ModelAdmin):
     list_display = ('fio', 'stud_ticket', 'birth_date', 'group')
     list_filter = ('group',)
     search_fields = ['fio', 'group']


class ModelLogAdmin(admin.ModelAdmin):
    list_display = ('model', 'target_instance', 'action', 'change_timestamp', )
    list_filter = ('model', 'action', 'change_timestamp', )
    search_fields = ['model']




admin.site.register(Groups, GroupsAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(ModelLog, ModelLogAdmin)
