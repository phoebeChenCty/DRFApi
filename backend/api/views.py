from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.forms.models import model_to_dict
import json

from products.models import Product
# the client want json file as reponse


# def api_home(request: WSGIRequest, *args, **kwargs):
#     body = request.body  # byte string json data
#     data = {}
#     try:
#         data = json.loads(body)  # string of json data -> python Dict
#     except:
#         pass
#     # return JsonResponse({"message": "Hi there, this is your Django API reponses!!"})
#     data['params'] = dict(request.GET)  # url query params
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)

def api_home(request: WSGIRequest, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    assert isinstance(model_data, Product)
    data = {}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # serialization, model instance->python dict->return JSON to client
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)
