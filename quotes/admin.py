from django.contrib import admin
from .models import Quote, OpenOrder
# from .models import AppUser

# Register your models here.

admin.site.register(Quote)
admin.site.register(OpenOrder)
# admin.site.register(AppUser)