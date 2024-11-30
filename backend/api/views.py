from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Products
from django.forms.models import model_to_dict

# Create your views here.

def api_response(request):
    models_data = Products.objects.all().order_by('?').first()

    data = {}
    if models_data:
        # data['id'] = models_data.id
        # data['title'] = models_data.title
        # data['content'] = models_data.content
        # data['price'] = models_data.price
        
        data = model_to_dict(models_data, fields=['id', 'title', 'price'])

        # model instance => model_data
        # turn into a python Dict
        # return JSON to my client
    return JsonResponse(data)
