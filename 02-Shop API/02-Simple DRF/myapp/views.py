from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


## Regular routes
# @api_view(['POST', 'GET'])
# def products(request):
#     return Response('list of the products', status=status.HTTP_200_OK)


## Routing to a class method
# class Shop():
#     @staticmethod
#     @api_view()
#     def products(request):
#         return Response({'message':'list of products!'}, 200)


## Routing class-based views
# from rest_framework.views import APIView
# class Shop(APIView):
#     def get(self, request, pk):
#         return Response({"message":"single product with id " + str(pk)}, status.HTTP_200_OK)
    
#     def patch(self, request, pk):
#     	return Response({"name":request.data.get('name')}, status.HTTP_200_OK)


## Routing classes that extend viewsets
# from rest_framework import viewsets
# class Shop(viewsets.ViewSet):
#     def list(self, request):
#     	return Response({"message":"All products"}, status.HTTP_200_OK)
#     def create(self, request):
#         return Response({"message":"Creating a product"}, status.HTTP_201_CREATED)
#     def update(self, request, pk=None):
#     	return Response({"message":"Updating a product"}, status.HTTP_200_OK)
#     def retrieve(self, request, pk=None):
#     	return Response({"message":"Displaying a product"}, status.HTTP_200_OK)
#     def partial_update(self, request, pk=None):
#         return Response({"message":"Partially updating a product"}, status.HTTP_200_OK)
#     def destroy(self, request, pk=None):
#     	return Response({"message":"Deleting a product"}, status.HTTP_200_OK)
