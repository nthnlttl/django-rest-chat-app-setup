from django.shortcuts import render
from rest_framework import generics
from .models import Message, Room

# Create your views here.

class MessageListAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()

class MessageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()

class RoomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()

class RoomListAPIView(generics.ListCreateAPIView):
    queryset = Room.objects.all()


