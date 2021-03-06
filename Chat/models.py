from django.db import models
from django.conf import settings

# Create your models here.

class Room(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class Message(models.Model):
    body = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.body

