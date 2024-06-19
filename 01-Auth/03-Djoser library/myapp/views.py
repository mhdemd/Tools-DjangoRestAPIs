from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Group
from .models import CustomUser


@api_view(['POST', 'DELETE'])
@permission_classes([IsAdminUser])
def managers(request):
    email = request.data.get('email')
    if email:
        user = get_object_or_404(CustomUser, email=email)
        managers = Group.objects.get(name="Manager")
        if request.method == 'POST':
            managers.user_set.add(user)
        if request.method == 'DELETE':
            managers.user_set.remove(user)
        return Response({"message": "Ok"}, status=status.HTTP_200_OK)

    return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)
