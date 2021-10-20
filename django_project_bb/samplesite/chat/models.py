from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.ForeignKey('Room', on_delete=models.CASCADE, null=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ('date_added',)
        verbose_name_plural = "Сообщения"
        verbose_name = "Сообщение"


class Room(models.Model):
    member_first = models.ForeignKey(User, related_name='member_first', on_delete=models.CASCADE, null=True)
    member_second = models.ForeignKey(User, related_name='member_second', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.member_first} - {self.member_second}'

    class Meta:
        verbose_name_plural = "Комнаты"
        verbose_name = "Комната"
