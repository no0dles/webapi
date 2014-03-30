from webapi.http.response import HttpResponse
from webapi.core.auth import allowed_roles


class MyEndpoint(object):
    #@allowed_roles(['Admin'])
    def get(self, request):
        return HttpResponse(
            """
            <form enctype="multipart/form-data" action="save_file.py" method="post">
            <p>File: <input type="file" name="file"></p>
            <p><input type="submit" value="Upload"></p>
            </form>
            """, headers={'Content-Type': 'text/html'})

    def post(self, request):
        return HttpResponse({'server': request.json})