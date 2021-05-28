from rest_framework import serializers
from .models import *


class CategorySerilizers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category


class ProductSerilizers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'Name',
            'price',
            'cat_id',
            'quantity'
        )
        model = Product


class CartSerializer(serializers.ModelSerializer):
    products = ProductSerilizers(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = ('cart_id', 'created_at', 'products')