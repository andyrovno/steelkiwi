MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=kiwi_testjob.settings $(MANAGE) test kiwi_students

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=kiwi_testjob.settings $(MANAGE) syncdb --noinput

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=kiwi_testjob.settings $(MANAGE) runserver

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=kiwi_testjob.settings $(MANAGE) migrate kiwi_students

