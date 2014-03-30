class Router(object):
    def __init__(self):
        self.routes = []

        #load all routes from urls.py
        self.load_urls()

    def load_urls(self):
        #get content of urls.py
        patterns = self.get_class('urls.urlpatterns')

        #add all routes and compile the regex
        import re
        for regex, endpoint in patterns:
            self.routes.append((re.compile(regex), self.get_class(endpoint)))

    def get_endpoint(self, request):

        for regex, endpoint in self.routes:
            #compare the request url path with the endpoint regex
            match = regex.match(request.path_info)
            if match:
                #if url matches return new instance of endpoint
                return endpoint()

        return None

    def get_endpoint_method(self, request):
        #get endpoint instance
        endpoint_instance = self.get_endpoint(request)

        #if endpoint instance was found
        if endpoint_instance:
            try:
                #get and execute endpoint method
                return getattr(endpoint_instance, request.method.lower())(request)
            except AttributeError:
                #do nothing if method does not exist
                pass

        return None

    def get_class(self, kls):
        parts = kls.split('.')
        module = ".".join(parts[:-1])

        m = __import__(module)
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m
