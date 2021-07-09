from rest_framework import viewsets
from rest_framework.serializers import Serializer
from . import models
from . import serializers

#per the video
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer

class QuoteViewset(viewsets.ModelViewSet):
    queryset = models.Quote.objects.all()
    serializer_class = serializers.QuoteSerializer

class AppUserViewset(viewsets.ModelViewSet):
    queryset = models.AppUser.objects.all()
    serializer_class = serializers.AppUserSerializer

# list(), retrieve(), create(), update(), destroy()


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context = self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })



# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        print('line 43')
        print(request.data)
        serializer = self.get_serializer(data = request.data)
        print('line 46')
        print(serializer)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        print(user)
        # print(request.META)
        # request.session['username'] = user
        return Response({
            "user": UserSerializer(user, context = self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        # return super().get_object()
        return self.request.user