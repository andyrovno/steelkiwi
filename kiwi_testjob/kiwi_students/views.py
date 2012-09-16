# -*- coding: utf-8 -*-
from django.views.generic.simple import direct_to_template
from django.db.models import Count
from django.utils import simplejson
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from models import Groups, Students
from forms import StudentsForm, GroupsForm

@login_required
def groups_overview(request):
     groups = Groups.objects.select_related('starosta').annotate(num_students=Count('st_group')).all()
     response_dict = {'groups': groups, 'user': request.user}
     return direct_to_template(request, 'groups_overview.html',
                               response_dict)

@login_required
def students_overview(request):
     try:
          group = request.GET['gr'].encode('utf-8')
     except:
          group = None
     if group:
          students_by_group = Students.objects.filter(group=int(group))
     return direct_to_template(request, 'students_overview.html',
                               {'students_by_group': students_by_group, 'user': request.user})

@login_required
def remove_group_or_student(request):
     results = {}
     if request.method == "POST" and request.is_ajax():
          if 'group_id' in request.POST and request.POST['group_id']:
               try:
                    Groups.objects.get(pk=request.POST['group_id'].encode('utf-8')).delete()
                    results['success'] = True
               except:
                    results['success'] = False
               json = simplejson.dumps(results, ensure_ascii=False)
          elif 'student_id' in request.POST and request.POST['student_id']:
               try:
                    Students.objects.get(pk=request.POST['student_id'].encode('utf-8')).delete()
                    results['success'] = True
               except:
                    results['success'] = False
               json = simplejson.dumps(results, ensure_ascii=False)
     return HttpResponse(json, mimetype='application/json')

@login_required
def edit_students_or_groups(request):
     if 'stid' in request.GET and request.GET['stid']:
          group_instance = None
          grid = ''
          template = 'edit_student.html'
          try:
               stid = request.GET['stid'].encode('utf-8')
               student_instance = Students.objects.get(pk=stid)
          except:
               student_instance = None
     elif 'grid' in request.GET and request.GET['grid']:
          student_instance  = None
          stid = ''
          template = 'edit_group.html'
          try:
               grid = request.GET['grid'].encode('utf-8')
               group_instance = Groups.objects.get(pk=grid)
          except:
               group_instance = None
     if request.method == "POST":
          if 'stud_ticket' in request.POST:
               form = StudentsForm(request.POST, instance=student_instance,
                                   auto_id=False)
          elif 'starosta' in request.POST:
               form = GroupsForm(request.POST, instance=group_instance,
                                 auto_id=False)
          response_dict = {}
          if request.is_ajax():
               if form.is_valid():
                    form.save()
                    response_dict['message'] = 'Changes have been saved'
                    response_dict['result'] = 'success'
               else:
                    response_dict['result'] = 'error'
                    response = {}
                    for error in form.errors:
                         response[error] = form.errors[error][0]
                    response_dict['response'] = response
               json = simplejson.dumps(response_dict, ensure_ascii=False)
               return HttpResponse(json, mimetype='application/json')
          else:
               if form.is_valid():
                    form.save()
     else:
          if student_instance:
               form = StudentsForm(instance=student_instance)
          elif group_instance:
               form = GroupsForm(instance=group_instance)
     return direct_to_template(request, template,
                               {'form':form, 'stid':stid, 'grid': grid})
          

def add_new_group(request):
     if request.method == "POST":
          form = GroupsForm(request.POST, auto_id=False)
          response_dict = {}
          if request.is_ajax():
               if form.is_valid():
                    form.save()
                    response_dict['message'] = 'Changes have been saved'
                    response_dict['result'] = 'success'
               else:
                    response_dict['result'] = 'error'
                    response = {}
                    for error in form.errors:
                         response[error] = form.errors[error][0]
                    response_dict['response'] = response
               json = simplejson.dumps(response_dict, ensure_ascii=False)
               return HttpResponse(json, mimetype='application/json')
          else:
               if form.is_valid():
                    form.save()
     form = GroupsForm()
     return direct_to_template(request, "add_group.html",
                               {'form':form})
@login_required
def add_new_student(request):
     if request.method == "POST":
          form = StudentsForm(request.POST, auto_id=False)
          response_dict = {}
          if request.is_ajax():
               if form.is_valid():
                    form.save()
                    response_dict['message'] = 'Changes have been saved'
                    response_dict['result'] = 'success'
               else:
                    response_dict['result'] = 'error'
                    response = {}
                    for error in form.errors:
                         response[error] = form.errors[error][0]
                    response_dict['response'] = response
               json = simplejson.dumps(response_dict, ensure_ascii=False)
               return HttpResponse(json, mimetype='application/json')
          else:
               if form.is_valid():
                    form.save()
     form = StudentsForm()
     return direct_to_template(request, "add_student.html",
                               {'form':form})
