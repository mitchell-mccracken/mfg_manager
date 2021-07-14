from django.contrib import admin
from .models import Quote, OpenOrder

# Register your models here.

admin.site.register(Quote)
admin.site.register(OpenOrder)