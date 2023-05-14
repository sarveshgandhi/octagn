from django.http import JsonResponse


def hello_world(request):
    message = {"message": "Hello, world!"}
    return JsonResponse(message)


def slash_hello_world(request):
    message = {"message": "/Hello, world with a slash"}
    return JsonResponse(message)
