from rest_framework.serializers import ModelSerializer
from .models import Category, OrderList, Product


class OrderListSerializer(ModelSerializer):
    class Meta:
        model = OrderList
        fields = ['id', 'name', 'images', 'created_date', 'category']

