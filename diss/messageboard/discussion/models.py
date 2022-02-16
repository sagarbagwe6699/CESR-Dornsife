from multiprocessing import AuthenticationError
from statistics import mode
from django.db import models

# Create your models here.


class Thread(models.Model):
    primary_key = models.IntegerField(default=1)
    week = models.CharField(max_length=100)
    topic = models.CharField(max_length=2000)
    messages = models.TextField(null=True)
    inforgraphic_text = models.TextField(
        default='Acceso a Infografía de esta semana', max_length=255, null=True, blank=True)
    infographic_link = models.TextField(default='', null=True, blank=True)
    # A message will have:
    #     1. Author
    #     2. Message
    #     3. Timestamp

    def __str__(self):
        return '{} - {}'.format(self.week, self.topic)


class ChatMessage(models.Model):
    author = models.CharField(max_length=30)
    week = models.CharField(max_length=100, null=True)
    message = models.TextField()
    time_stamp = models.DateField()

    def __str__(self):
        return 'Week -> {} | Author -> {} | Message -> {}...'.format(self.week, self.author, self.message[:20])
