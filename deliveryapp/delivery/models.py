from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user/%Y/%m', default=None)


class ModelBase(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(ModelBase):
    name = models.CharField(max_length=99, null=False)
    cmnd = models.CharField(null=False, max_length=10)
    number_phone = models.CharField(max_length=10, null=False)
    avatar = models.ImageField(upload_to='customer/%Y/%m', default=None)

    def __str__(self):
        return self.name


class Deliver(ModelBase):
    name = models.CharField(max_length=99, null=False)
    cmnd = models.CharField(null=False, max_length=10)
    number_phone = models.CharField(max_length=10, null=False)
    avatar = models.ImageField(upload_to='customer/%Y/%m', default=None)

    def __str__(self):
        return self.name


class Category(ModelBase):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Order_list(ModelBase):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'category')


class Product(ModelBase):
    name = models.CharField(max_length=255, null=False)
    images = models.ImageField(upload_to='product/%Y/%m', default=None)
    price = models.DecimalField(decimal_places=6, max_digits=10)
    content = RichTextField()
    order_list = models.ForeignKey(Order_list,
                                   related_name='products',
                                   related_query_name='my_product',
                                   on_delete=models.CASCADE)
    hashtags = models.ManyToManyField('Hashtag')

    def __str__(self):
        return self.name


class Comment(ModelBase):
    content = models.TextField()
    product = models.ForeignKey(Product,
                                related_name='comments',
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deliver = models.ForeignKey(Deliver, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Hashtag(ModelBase):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
