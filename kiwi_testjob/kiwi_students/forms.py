from django import forms
from django.forms import ModelForm

from models import Students, Groups


class StudentsForm(ModelForm):
     def __init__(self, *args, **kwargs):
          super(StudentsForm, self).__init__(*args, **kwargs)

     class Media:
          js = ("/static/js/jquery.form_3.09.js",
               "/static/js/edit_form_student_or_group.js",)

     class Meta:
          model = Students


class GroupsForm(ModelForm):
     def __init__(self, *args, **kwargs):
          super(GroupsForm, self).__init__(*args, **kwargs)

     class Media:
          js = ("/static/js/jquery.form_3.09.js",
                "/static/js/edit_form_student_or_group.js",)

     class Meta:
          model = Groups
