from rest_framework.response import Response
from rest_framework import status


## viewsets.ViewSet
from rest_framework import viewsets
class Shop(viewsets.ViewSet):
    def list(self, request):
    	return Response({"message":"All products"}, status.HTTP_200_OK)
    def create(self, request):
        return Response({"message":"Creating a product"}, status.HTTP_201_CREATED)
    def update(self, request, pk=None):
    	return Response({"message":"Updating a product"}, status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
    	return Response({"message":"Displaying a product"}, status.HTTP_200_OK)
    def partial_update(self, request, pk=None):
        return Response({"message":"Partially updating a product"}, status.HTTP_200_OK)
    def destroy(self, request, pk=None):
    	return Response({"message":"Deleting a product"}, status.HTTP_200_OK)
