from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django.shortcuts import get_object_or_404


# ===================================================== List of products
# API 38-39
@api_view()
def products(request):
    items = Product.objects.all()
    serialized_item = ProductSerializer(items, many=True)
    return Response(serialized_item.data)

# API 40, 41
@api_view()
def products(request):
    items = Product.objects.select_related('category').all()  
    serialized_item = ProductSerializer(items, many=True)
    return Response(serialized_item.data)

# API 42
@api_view()
def products(request):
    items = Product.objects.select_related('category').all()
    serialized_item = ProductSerializer(items, many=True, context={'request': request})
    return Response(serialized_item.data)

# ===================================================== Single product
@api_view()
def single_product(request, id):
    items = get_object_or_404(Product, pk=id)
    # items = Product.objects.get(pk=id)
    serialized_item = ProductSerializer(items)
    return Response(serialized_item.data)

# ===================================================== Nested category detail
# API 42
@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category,pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data)
