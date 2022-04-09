from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import User, Category, Product, OrderList, Hashtag


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


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OrderListSerializer(ModelSerializer):
    image = SerializerMethodField(source='image')

    class Meta:
        model = OrderList
        fields = ['id', 'name', 'image', 'created_date', 'category']

    def get_image(self, obj):
        request = self.context['request']
        path = '/static/%s' % obj.image.name

        return request.build_absobute_uri(path)


class HashTagSerializer(ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['id', 'name', 'created_date']


class ProductSerializer(ModelSerializer):
    image = SerializerMethodField(source='image')
    hashtags = HashTagSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'content', 'created_date', 'orderList', 'image', 'hashtags']

    def get_image(self, obj):
        request = self.context['request']
        path = '/static/%s' % obj.image.name

        return request.build_absobute_uri(path)
