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
    # category = CategroSerializer()  # API 40
    # category = serializers.StringRelatedField()  # API 38, 39
    category = serializers.HyperlinkedRelatedField(
        queryset = Category.objects.all(),
        view_name='category-detail'
    )  # API 43
    class Meta:
        model = Product
        fields = [
            'id',
            'web_id',
            'slug',
            'name',
            'description',
            'category',
        ]
        # depth = 1  # API 41

    def validate(self, data):
        if 'name' in data and not data.get('slug'):
            data['slug'] = slugify(data['name'])
        return data
