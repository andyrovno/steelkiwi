from django.db import connection
from django.template import Template, Context
from django.utils.encoding import force_unicode

class SQLCalc:
    def process_response ( self, request, response ): 
        time = 0.0
        for q in connection.queries:
		time += float(q['time'])
        t = Template('''
            <p><i>Sql requests:</i> {{ count }}<br/>
            <i>Time spent:</i> {{ time }}</p>
        ''')
        if response.get("content-type", "").startswith("text/html"):
            stat = "%s" % t.render(Context({'count':len(connection.queries),'time':time}))
            response.content = "%s" % force_unicode(response.content).replace('</body>', stat + '\n</body>' )
        return response
