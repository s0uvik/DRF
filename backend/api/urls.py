from django.urls import path
from . import views
# from .views import api_response

urlpatterns = [
    path('', views.api_response)
]
