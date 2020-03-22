from rest_framework import serializers
from rest_framework.serializers import ValidationError
from api.models import UserPost
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_active', 'is_staff', 'is_superuser',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            password=make_password(validated_data['password']),
            is_active=True,
            is_superuser=False,
            is_staff=True
        )
        user.save()

        return user


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user.is_active.__eq__(bool(True)):
                data['user'] = user
            else:
                raise ValidationError("Account is suspended!")
        else:
            raise ValidationError("Credentials are required!")

        return data


class UserPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPost
        fields = ('id', 'post_title', 'post_description', 'post_image', 'is_active', 'user',)
        read_only_fields = ('id', 'user', 'is_active', 'post_image',)