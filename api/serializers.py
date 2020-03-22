import re
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from api.models import UserPost
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_active', 'is_staff', 'is_superuser',)
        write_only_fields = ('password', 'username', 'email',)
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser',)

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
