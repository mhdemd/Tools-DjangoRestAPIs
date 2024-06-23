from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view()
def products(request):
    return Response('list of the products', status=status.HTTP_200_OK)

