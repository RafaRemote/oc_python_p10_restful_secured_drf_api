from rest_framework import serializers
from user.models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
                                     min_length=8,
                                     max_length=64,
                                     write_only=True
                                     )

    class Meta:
        model = User
        fields = [
                  'first_name',
                  'last_name',
                  'email',
                  'password'
                  ]

    def validate(self, attrs):
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')

        if not first_name.isalnum() or not last_name.isalnum():
            raise serializers.ValidationError(
                'names: names should only contain alphanumeric characters')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
                                       min_length=8,
                                       max_length=255,
                                       read_only=True
                                       )
    email = serializers.EmailField(
                                   min_length=7,
                                   max_length=255
                                   )
    password = serializers.CharField(
                                     min_length=8,
                                     max_length=60,
                                     write_only=True
                                     )
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = [
                  'email',
                  'password',
                  'first_name',
                  'tokens'
                  ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(
                                 email=email,
                                 password=password
                                 )
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        return {
            'email': user.email,
            'first_name': user.first_name,
            'tokens': user.tokens
        }
