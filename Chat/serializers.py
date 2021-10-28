from rest_framework import serializers

from .models import Message, Room

class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = ('id', 'user', 'message')

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('id', 'title')


