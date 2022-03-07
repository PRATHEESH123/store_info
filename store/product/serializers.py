# django rest framework
from rest_framework import serializers

# local
from .models import Product,Category,Sub_Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class Sub_CategorySerializer(serializers.ModelSerializer):
    category=CategorySerializer()

    class Meta:
        model = Sub_Category
        fields = (
            'id',
            'name',
            'category',
        )


class ProductSerializer(serializers.ModelSerializer):
    sub_category = Sub_CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'sub_category',
            'descrption',
            'stock',
            'price',
            'false_price',
        )