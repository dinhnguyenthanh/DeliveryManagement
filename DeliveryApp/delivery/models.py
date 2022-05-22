from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField


class User(AbstractUser):
    pass


class ModelBase(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Shipper(ModelBase):
    user_type = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, upload_to='shippers/%Y/%m')

    def __str__(self):
        return self.user_type


class Customer(ModelBase):
    user_type = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_type


class Category(ModelBase):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class CategoryItem(ModelBase):
    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(null=True, blank=True, upload_to='categoryItems/%Y/%m')
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ('name', 'category')
        ordering = ['id']

    def __str__(self):
        return self.name


class Goods(ModelBase):
    name = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(null=True, blank=True, upload_to='goods/%Y/%m')
    category_item = models.ForeignKey(CategoryItem,
                                      related_name='goodss',
                                      related_query_name='my goods',
                                      on_delete=models.CASCADE)

    def __str__(self):
        return self.name
