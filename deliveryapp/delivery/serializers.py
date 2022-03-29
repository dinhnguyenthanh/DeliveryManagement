from rest_framework.serializers import ModelSerializer
from .models import Category, OrderList, Product, Hashtag, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'avatar']
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user


class OrderListSerializer(ModelSerializer):
    class Meta:
        model = OrderList
        fields = ['id', 'name', 'images', 'created_date', 'category']


class HashTagSerializer(ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['id', 'name', 'created_date']


class ProductSerializer(ModelSerializer):
    hashtags = HashTagSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'content', 'created_date', 'orderList', 'images', 'hashtags']


