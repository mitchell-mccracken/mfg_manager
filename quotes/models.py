from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.fields import CharField

# Create your models here.

class Quote(models.Model):
    q_title = models.CharField(max_length=200)
    # q_date_created = models.DateTimeField('date published')
    q_date_created = models.DateTimeField(default=datetime.now)
    customer_name = models.CharField(max_length=200 , default='none')
    contact_name = models.CharField(max_length=200 , default='none', blank=True)
    customer_address = models.CharField(max_length=400 , default='none')
    contact_phone = models.CharField(max_length=15, default='867-5309', blank=True)
    lead_time = models.CharField(max_length=100, default='N/A')
    part_number = models.CharField(max_length=100, default='N/A')
    part_description = models.CharField(max_length=100, default='N/A')
    part_qty = models.CharField(max_length=100, default='0')
    part_cost = models.DecimalField(max_digits=6, decimal_places=2, default='0.00')
    q_accepted = models.BooleanField(default=False)
    date_accepted = models.CharField(max_length=100, default='N/A')
    # quote_total = models.CharField(max_length=20, default='N/A', blank=True)
    quote_total = models.DecimalField(max_digits=6, decimal_places=2, default='0.00')
    quote_notes = models.CharField(max_length=500, default='', blank=True)
    def __str__(self):
        return self.q_title

class OpenOrder(models.Model):
    q_id = models.CharField(max_length=10)
    o_title = models.CharField(max_length=200)
    o_start_date = models.DateTimeField(default=datetime.now)


#comment
# class AppUser(models.Model):
#     user= models.OneToOneField(User, on_delete=models.CASCADE)
#     department = models.CharField(max_length=100)