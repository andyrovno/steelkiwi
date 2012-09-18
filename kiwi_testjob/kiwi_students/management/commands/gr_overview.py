from django.core.management.base import NoArgsCommand
from kiwi_testjob.kiwi_students.models import Students, Groups


class Command( NoArgsCommand ):
     requires_model_validation = True

     def handle_noargs(self, **options):
          lines = []
          groups = Groups.objects.select_related('starosta')
          for group in groups:
               lines.append("[%s]" % group.namegr)
               kod = group.id
               studs = Students.objects.select_related('gruppa').filter(group=kod)
               for stud in studs:
                    lines.append(" --- %s" % stud.fio + "\n")
          return "\n".join( lines )
