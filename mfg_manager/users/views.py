from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def users_page(request):
    return HttpResponse("Hellow, world. this is the users page")