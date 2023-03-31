from django.db import models
from django.contrib.auth.models import User

class ChatUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Добавьте дополнительные поля, если это необходимо
    # ...

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
