from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user/%Y/%m', null=True)

    class Meta:
        ordering = ["id"]


class ModelBase(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(ModelBase):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]


class OrderList(ModelBase):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    images = models.ImageField(upload_to='orderList/%Y/%m', null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'category')
        ordering = ["id"]


class Product(ModelBase):
    name = models.CharField(max_length=255, null=False)
    images = models.ImageField(upload_to='product/%Y/%m', null=True)
    price = models.DecimalField(decimal_places=0, max_digits=10)
    content = RichTextField()
    orderList = models.ForeignKey(OrderList,
                                  related_name='products',
                                  related_query_name='my_product',
                                  on_delete=models.CASCADE)
    hashtags = models.ManyToManyField('Hashtag')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]


class Comment(ModelBase):
    content = models.TextField()
    product = models.ForeignKey(Product,
                                related_name='comments',
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["id"]


class Hashtag(ModelBase):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]


class ActionBase(ModelBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'product')
        abstract = True


class Like(ActionBase):
    active = models.BooleanField(default=True)


class Rating(ActionBase):
    rate = models.SmallIntegerField(default=0)



