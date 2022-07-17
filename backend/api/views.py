from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.forms.models import model_to_dict
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer
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

# def api_home(request: WSGIRequest, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     assert isinstance(model_data, Product)
#     data = {}
#     if model_data:
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
#         # serialization, model instance->python dict->return JSON to client
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#     return JsonResponse(data)

# @api_view(["GET", "POST"])
# @api_view(["GET"])
# def api_home(request: WSGIRequest, *args, **kwargs):
#     # if request.method != "POST":
#     #     return Response({"detail": "GET not allowed"}, status=405)
#     model_data = Product.objects.all().order_by("?").first()
#     assert isinstance(model_data, Product)
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#     return Response(data)

# @api_view(["POST"])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         # data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#         data = ProductSerializer(instance).data
#     return Response(data)

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    # check if an instance (Product) can be create successfully
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save() # add new instance to database, create a database instance by default value /input value
        # print("instance: ", instance)
        data = serializer.data
        print("data: ", data)
        return Response(data)
    return Response({"invalid": "not good data"}, status=400)
