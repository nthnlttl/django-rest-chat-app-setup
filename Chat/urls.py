from django.urls import path 

from . import views

urlpatterns = [
    path('messages/<int:pk>/', views.MessageDetailAPIView.as_view()), # details of a specific message GET PUT DELETE
    path('rooms/<int:pk>/', views.RoomDetailAPIView.as_view()), # details of a specific room GET PUT DELETE
    path('rooms/', views.RoomListAPIView.as_view()), # all rooms GET POST
]