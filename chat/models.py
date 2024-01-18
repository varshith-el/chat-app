from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    users = models.ManyToManyField(User)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
