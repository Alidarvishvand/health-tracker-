from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = get_user_model()
        fields = [ 'id','username', 'email']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)


    class Meta: 
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password_confirmation']

        def validate(self,data):
            if data['password'] != data['password_confirmation']:
                raise serializers.ValidationError("Password must match")
            return data
        
        def create(self, validated_data):
            user = get_user_model().objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
            )
            return user