from webapi.http.response import HttpResponse
from webapi.core.auth import allowed_roles, requires_auth


class MyEndpoint(object):
    @allowed_roles(roles=['Admin'])
    def get(self, request):
        return HttpResponse({'echo': 'hi'})

    @requires_auth
    def post(self, request):
        return HttpResponse({'server': request.json})