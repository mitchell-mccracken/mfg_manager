from django.urls import path

from . import views

urlpatterns = [
    path('' , views.users_page, name='users_page')
]