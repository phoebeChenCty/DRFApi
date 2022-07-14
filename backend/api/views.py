from django.http import JsonResponse

# the client want json file as reponse


def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Hi there, this is your Django API reponses!!"})
