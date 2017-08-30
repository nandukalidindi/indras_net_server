from django.http import JsonResponse

def index(request):
    return JsonResponse({'foo':'bar'})

def get_agent(request):
    return JsonResponse({'agent': {}})

def get_matches(request):
    return JsonResponse({'matches': []})

def book(request):
    return JsonResponse({'success': {}})

def cancel(request):
    return JsonResponse({'success': {}})
