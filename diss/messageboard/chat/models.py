from multiprocessing import AuthenticationError
from django.db import models

# Create your models here.


class usermessage(models.Model):
    author = models.CharField(max_length=30)
    text = models.TextField()
    time = models.DateField()

    def __str__(self):
        return self.author
