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
        ##================== filtering
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price)
            # items = items.filter(price__lte=to_price)  # exact price
        ##================== searching
        search = request.query_params.get('search')
        if search:
            items = items.filter(name__startswith=search)
            # items = items.filter(name__contains=search)  # any where on name
            # items = items.filter(name__icontains=search)  # any where on name & case sensitive
        ##================== ordering
        ordering = request.query_params.get('ordering')
        if ordering:
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)
            
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
