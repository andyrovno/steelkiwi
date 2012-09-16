from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout

from kiwi_students.views import groups_overview, students_overview,\
     remove_group_or_student, edit_students_or_groups,add_new_group,\
     add_new_student


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', groups_overview, name='homepage'),
    url(r'^students/$', students_overview, name='students'),
    url(r'^rmgroup/$', remove_group_or_student, name='remove_group_or_student'),
    url(r'^edit/student/$', edit_students_or_groups, name='edit_stud'),
    url(r'^edit/group/$', edit_students_or_groups, name='edit_group'),
    url(r'^add/group/', add_new_group, name="add_group"),
    url(r'^add/student/', add_new_student, name="add_student"),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    # Examples:
    # url(r'^$', 'kiwi_testjob.views.home', name='home'),
    # url(r'^kiwi_testjob/', include('kiwi_testjob.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
)
