from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.ForeignKey('Room', on_delete=models.CASCADE, null=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

class Room(models.Model):
    member_first = models.ForeignKey(User, related_name='member_first', on_delete=models.CASCADE, null=True)
    member_second = models.ForeignKey(User, related_name='member_second', on_delete=models.CASCADE, null=True)