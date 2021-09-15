from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='message/')
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-timestamp',)
