from rest_framework import serializers
from .models import Category, CategoryItem, Goods


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, obj):
        request = self.context['request']
        path = '/static/%s' % obj.image.name

        return request.build_absolute_uri(path)

    class Meta:
        model = CategoryItem
        fields = ['id', 'name', 'created_date', 'image', 'category_id']


class GoodsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, obj):
        request = self.context['request']
        path = '/static/%s' % obj.image.name

        return request.build_absolute_uri(path)

    class Meta:
        model = Goods
        fields = ['id', 'name', 'created_date', 'updated_date', 'image']
