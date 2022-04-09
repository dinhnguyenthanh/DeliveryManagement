from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import User, Category, Product, OrderList, Hashtag, Comment


class UserSerializer(ModelSerializer):
    avatar = SerializerMethodField(source='avatar')

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

    def get_avatar(self, obj):
        request = self.context['request']
        path = '/static/%s' % obj.avatar.name

        return request.build_absolute_uri(path)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OrderListSerializer(ModelSerializer):
    image = SerializerMethodField(source='image')

    class Meta:
        model = OrderList
        fields = ['id', 'name', 'image', 'created_date', 'category_id']

    def get_image(self, obj):
        request = self.context['request']
        path = '/static/%s' % obj.image.name

        return request.build_absolute_uri(path)


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

        return request.build_absolute_uri(path)


class CreateCommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'product']


class CommentSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        exclude = ['active']
