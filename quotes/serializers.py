from rest_framework import serializers
from .models import OpenOrder, Quote
# from .models import AppUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

class OpenOrderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = OpenOrder
        fields= '__all__'

# class AppUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AppUser 
#         fields ='__all__'


#User Serailizer
# from -> https://www.youtube.com/watch?v=0d7cIfiydAc 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username' , 'email')


#Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username' , 'email', 'password')
        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'] , validated_data['email'] , validated_data['password'])
        return user

#Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Inccorect Credentials")