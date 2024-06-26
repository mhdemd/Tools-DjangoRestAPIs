from rest_framework import serializers
from myapp.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'web_id', 'slug', 'name', 'description', 
            'is_active', 'created_at', 'updated_at'
        ]
