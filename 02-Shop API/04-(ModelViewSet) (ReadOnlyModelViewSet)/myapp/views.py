from rest_framework import viewsets
from myapp.models import Product
from myapp.serializers import ProductSerializer


## viewsets.ModelViewSet
# class Shop(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


## viewsets.ReadOnlyModelViewSet
class Shop(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
