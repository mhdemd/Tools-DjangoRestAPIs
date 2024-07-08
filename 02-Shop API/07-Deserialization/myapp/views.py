from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404


# ===================================================== List of products
@api_view(['GET', 'POST'])
def products(request):
    if request.method == "GET":
        items = Product.objects.select_related('category').all()  
        serialized_item = ProductSerializer(items, many=True)
        return Response(serialized_item.data)
    if request.method == "POST":
        serialized_item = ProductSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)


# ===================================================== Single product
@api_view()
def single_product(request, id):
    items = get_object_or_404(Product, pk=id)
    serialized_item = ProductSerializer(items)
    return Response(serialized_item.data)
