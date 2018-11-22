import os, sys
from django.core.wsgi import get_wsgi_application

# put the full path to the project below
sys.path.append("path/to/project's/root/dir")

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

application = get_wsgi_application()