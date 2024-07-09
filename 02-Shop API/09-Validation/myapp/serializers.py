from rest_framework import serializers
from .models import Product, Category
from django.utils.text import slugify
from rest_framework.validators import UniqueValidator
from rest_framework.validators import UniqueTogetherValidator


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
    
    ## ================= API 47: Conditions in the field
    # price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=2)

    ## ================= API 51 -> method 2: UniqueValidator
    # name = serializers.CharField(
    #         max_length=255,
    #         validators=[UniqueValidator(queryset=Product.objects.all())]
    #     )
    
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
        
        ## ================= API 48: Using keyword arguments in the Meta class
        # extra_kwargs = {
        #     'price': {
        #         'min_value': 2,
        #         'max_digits': 6,
        #         'decimal_places': 2,
        #         'error_messages': {
        #             'max_digits': 'Price cannot have more than 6 digits in total.',
        #             'decimal_places': 'Price cannot have more than 2 decimal places.',
        #             'min_value': 'Price must be at least 2.',
        #         },
        #     },
        # }
        
        ## ================= API 51 -> method 1: UniqueValidator
        # extra_kwargs = {
        #         'name': {
        #             'validators': [
        #                 UniqueValidator(
        #                     queryset=Product.objects.all()
        #                     )
        #                 ]
        #             }
        #         }

        ## ================= API 52: UniqueTogetherValidator
        validators = [
            UniqueTogetherValidator(
                queryset=Product.objects.all(),
                fields=['name', 'price']
            ),
        ]

    ## ================= API 49: Using validate_field() method 
    # def validate_price(self, value):
    #     if value < 5:
    #         raise serializers.ValidationError("Price must be at least 5.")
    #     if value.as_tuple().exponent < -1:
    #         raise serializers.ValidationError("Price cannot have more than 1 decimal places.")
    #     if len(str(value).replace('.', '')) > 5:
    #         raise serializers.ValidationError("Price cannot have more than 5 digits in total.")
    #     return value
        
    def validate(self, data):
        ## ================= API 50: Using the validate() method    
        # value = data['price']
        # if value < 2:
        #     raise serializers.ValidationError('Price should not be less than 2.0')
        # if value.as_tuple().exponent < -1:
        #     raise serializers.ValidationError({"price": "Price cannot have more than 1 decimal places."})
        # if len(str(value).replace('.', '')) > 5:
        #     raise serializers.ValidationError({"price": "Price cannot have more than 5 digits in total."})
        
        if 'name' in data and not data.get('slug'): 
            data['slug'] = slugify(data['name'])
        return super().validate(data)
