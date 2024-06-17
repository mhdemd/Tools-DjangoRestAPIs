from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class RegisterView(generics.CreateAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    serializer_class = RegisterSerializer
