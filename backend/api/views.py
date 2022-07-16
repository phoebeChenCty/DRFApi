from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
import json
# the client want json file as reponse


def api_home(request: WSGIRequest, *args, **kwargs):
    body = request.body  # byte string json data
    data = {}
    try:
        data = json.loads(body)  # string of json data -> python Dict
    except:
        pass
    # return JsonResponse({"message": "Hi there, this is your Django API reponses!!"})
    data['params'] = dict(request.GET)  # url query params
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
