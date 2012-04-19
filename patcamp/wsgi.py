import os
import site

# the project's root directory (the one with manage.py)
root = lambda *a: os.path.join(os.path.dirname(__file__), '..', *a)

activate_this = root('..', 'env', 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

site.addsitedir(root())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patcamp.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
