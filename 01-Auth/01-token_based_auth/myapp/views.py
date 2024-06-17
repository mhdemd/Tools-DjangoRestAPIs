from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


# ========= Token based auth
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "some secret message!"})

# ========= User roles (Authorization)
@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name="Manager").exists():
        return Response({"message": "Only managers should see this!"})
    else:
        return Response({"message": "You are not authorized!!"}, 403)
    
# ======== Setting up API throttling
# Anon
@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message": "message for throttle_check (Anonymous)"})

# Users
@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def throttle_check_auth(request):
    return Response({"message": "message for throttle_check (Logged in users)"})
