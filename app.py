import os
os.environ.setdefault("WEBAPI_SETTINGS_MODULE", 'settings')

from webapi.core.wsgi import WSGIHandler
application = WSGIHandler()