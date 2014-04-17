import json


class HttpRequest(object):
    def __init__(self, environ):
        self.path_info = environ['PATH_INFO']
        self.request_uri = environ['REQUEST_URI']
        self.script_name = environ['SCRIPT_NAME']
        self.query_string = environ['QUERY_STRING']
        self.method = environ['REQUEST_METHOD']

        self.remote_addr = environ['REMOTE_ADDR']
        self.remote_port = environ['REMOTE_PORT']
        self.server_port = environ['SERVER_PORT']

        self.server_protocol = environ['SERVER_PROTOCOL']
        self.server_name = environ['SERVER_NAME']

        self.wsgi_multiprocess = environ['wsgi.multiprocess']
        self.wsgi_multithread = environ['wsgi.multithread']
        self.wsgi_url_scheme = environ['wsgi.url_scheme']
        self.wsgi_version = environ['wsgi.version']
        self.wsgi_run_once = environ['wsgi.run_once']

        self.content_type = environ.get('CONTENT_TYPE', '')

        self.body = None
        self.json = None

        self.user = None
        self.roles = []

        #get content-length if set
        try:
            self.content_length = int(environ.get('CONTENT_LENGTH', '0'))
        except ValueError:
            self.content_length = 0

        #if content-length is set load request body
        if self.content_length != 0:
            self.body = environ['wsgi.input'].read(self.content_length)

            #if content-type is json
            if 'application/json' in self.content_type:
                try:
                    #parse body to dict
                    self.json = json.loads(self.body)
                except ValueError:
                    pass
            elif 'multipart/form-data' in self.content_type:
                print self.body

        #load all http headers
        self.headers = {}
        for key in environ:
            if key.startswith('HTTP'):
                self.headers[key[5:]] = environ[key]

        """
            'wsgi.errors': <open file 'wsgi_errors', mode 'w' at 0x105bda6f0>,
            'wsgi.file_wrapper': <built-in function uwsgi_sendfile>,
        """