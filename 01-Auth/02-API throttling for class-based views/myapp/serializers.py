from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_email(self, value):
        # Verify that the email is not a duplicate
        User = get_user_model()
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value

    def validate(self, attrs):
        # Validate that the passwords match
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        
        # Validate the password using Django's built-in validators
        try:
            validate_password(attrs['password'])
        except ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})
        
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = get_user_model().objects.create_user(**validated_data)
        return user
