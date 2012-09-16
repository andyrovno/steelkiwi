from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
#from django_any import any_model

from kiwi_testjob.kiwi_students.models import Students, Groups
from kiwi_testjob.kiwi_students.forms import GroupsForm, StudentsForm


class TemplateContextProcTest(TestCase):
    """ Checking for django_settings in context """

    def setUp(self):
        self.client = Client()

    def test_context(self):
        user = self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('homepage'))
        self.assertTrue('django_settings' in response.context)


class StudentsGroupsCreationTest(TestCase):


    def setUp(self):
        self.client = Client()
        self.user = self.client.login(username='admin', password='admin')
        self.group_dict = {'namegr': "GR-TEST"}
        self.student_dict = {'fio': "Test S.T.",
                    'birth_date': "1986-12-20",
                    'stud_ticket': "0000000000"}


    def test_add_group(self):
        form_group = GroupsForm(self.group_dict)
        self.assertTrue(form_group.is_valid())
        group_obj = form_group.save(commit=False)
        group_obj.save()
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, self.group_dict['namegr'])
        form_student = StudentsForm(self.student_dict)
        self.assertTrue(form_student.is_valid())
        stud_obj = form_student.save(commit=False)
        stud_obj.group = Groups.objects.get(namegr=self.group_dict['namegr'])
        stud_obj.save()
        response = self.client.get(reverse('students') + '?gr=' + str(group_obj.pk))
        self.assertContains(response, self.student_dict['fio'])
        self.assertContains(response, self.student_dict['stud_ticket'])
