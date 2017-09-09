from django.http import JsonResponse
from indra import api

def index(request):
    agent = api.get_agent(1)
    return JsonResponse({'agent': agent})

def get_agent(request):
    return JsonResponse({'agent': {}})

def get_matches(request):
    return JsonResponse({'matches': []})

def book(request):
    return JsonResponse({'success': {}})

def cancel(request):
    return JsonResponse({'success': {}})
