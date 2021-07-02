from django.db import models
from datetime import datetime

# Create your models here.

class Quote(models.Model):
    q_title = models.CharField(max_length=200)
    # q_date_created = models.DateTimeField('date published')
    q_date_created = models.DateTimeField(default=datetime.now)
    customer_name = models.CharField(max_length=200 , default='none')
    contact_name = models.CharField(max_length=200 , default='none')
    customer_address = models.CharField(max_length=400 , default='none')
    def __str__(self):
        return self.q_title

