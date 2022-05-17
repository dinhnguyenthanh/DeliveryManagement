from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')
    id_number = models.CharField(max_length=12, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)


class Shipper(User):
    rating = models.IntegerField(default=0)


class Customer(User):
    pass


class DriverLicence(models.Model):
    pass


class Order(models.Model):
    pass

