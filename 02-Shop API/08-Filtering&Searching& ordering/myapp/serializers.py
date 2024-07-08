from rest_framework import serializers
from .models import Product, Category
from django.utils.text import slugify


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'slug',
            'title',
        ]

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'web_id',
            'slug',
            'name',
            'description',
            'price',
            'category',
            'category_id',
        ]

    def validate(self, data):
        if 'name' in data and not data.get('slug'):
            data['slug'] = slugify(data['name'])
        return data
