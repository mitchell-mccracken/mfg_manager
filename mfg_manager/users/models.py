from django.db import models
from datetime import datetime

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=datetime.now)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.username