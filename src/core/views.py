from django.http import JsonResponse


def index(request):
    return JsonResponse({'app': 'core', 'status': 'ok'})
