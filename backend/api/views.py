from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def api_response(request):
    body = request.body # byte string JSOn data
    print(request.GET)
    print(request.POST)
    data = {}
    try:
        data = json.loads(body) # string to JSON data => Python dict
    except:
        pass
    print(data)
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    data['content_type'] = request.content_type
    return JsonResponse(data)
