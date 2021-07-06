from rest_framework import viewsets
from . import models
from . import serializers

class QuoteViewset(viewsets.ModelViewSet):
    queryset = models.Quote.objects.all()
    serializer_class = serializers.QuoteSerializer

class AppUserViewset(viewsets.ModelViewSet):
    queryset = models.AppUser.objects.all()
    serializer_class = serializers.AppUserSerializer

# list(), retrieve(), create(), update(), destroy()

