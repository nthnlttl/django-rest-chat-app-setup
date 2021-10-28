from django.urls import path, include
from . import views

app_name = 'api_v1'

urlpatterns = [
    path('', include('messages.urls')),
]