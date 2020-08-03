from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions

from identity.models import User


class AuthTokenSerializer(serializers.Serializer):
    emailId = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get('emailId')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
        else:
            msg = _('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    last_name = serializers.CharField()
    first_name = serializers.CharField()

    class Meta:
        model = User
        fields = ("first_name", 'last_name',  'email', 'password',)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exist")
        return email


class ProfileUpdateSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField()
    lastName = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('email', 'firstName', 'lastName',)

    # def validate_email(self, email):
    #     if User.objects.all.filter(email=email).exclude.exists():
    #         return email
    #     raise serializers.ValidationError("Country code is not valid")
    #
    #
    # def create(self, validated_data):
    #     user = self.context.get('request').user
    #     if validated_data.get('email'):
    #         user.email=validated_data.get('email')
    #     if validated_data.get('firstName'):
    #         user.first_name = validated_data.get('firstName')
    #     if validated_data.get('lastName'):
    #         user.last_name = validated_data.get('lastName')
    #     user.save()
    #     return user
