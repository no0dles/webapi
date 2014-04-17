from webapi.core.route import Router
from webapi.http.request import HttpRequest
from webapi.http.response import NotFoundResponse


class WSGIHandler(object):
    def __init__(self):
        #init url resolver
        self.router = Router()

    def __call__(self, environ, start_response):
        #generate request from wsgi environment
        request = HttpRequest(environ)

        #check accept
        #TODO

        #resolve url and load response from endpoint
        response = self.router.get_endpoint_method(request)

        #if no response is set
        if not response:
            #return http 404
            response = NotFoundResponse()
        else:
            #if response is set and no content-type is set
            if not response.headers.get('Content-Type'):
                #set json as default content-type
                response.headers['Content-Type'] = 'application/json'

        #prepare wsgi response
        start_response(response.get_status_phrase(), response.get_headers())

        #return response body
        return response.get_body_response()

    def authorized(self):
        if 'Admin' in self.groups:
            return True

    def authentificate_user(self, request):
        return 'Pascal'

    def authentificate_group(self):
        return 'Admin'
