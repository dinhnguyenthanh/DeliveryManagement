from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField


class User(AbstractUser):
    last_login = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='uploads/%Y/%m')
    phone = models.CharField(max_length=10, null=False)
    date_of_birth = models.DateTimeField(blank=True, null=True)


class ModelBase(models.Model):
    class Meta:
        abstract = True

    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Shipper(User):
    class Meta:
        unique_together = ('driver_licence_number', 'driver_licence_class')

    face_image = models.ImageField(null=False, upload_to='shipper/%Y/%m')
    id_number = models.CharField(max_length=12, null=False, unique=True)
    driver_licence_number = models.CharField(max_length=12)
    driver_licence_class = models.CharField(max_length=4)

    # Thiết lập mối quan hệ One To One (Shipper - User)
    # user_ptr = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)

    # Thiết lập mối quan hệ Many (Shipper) to Many (Order) thông qua bảng Bargain
    orders = models.ManyToManyField('Order', through='Bargain')

    # Thiết lập mối quan hệ Many (Shipper) to Many (Customer) thông qua bảng Feedback
    customers = models.ManyToManyField('Customer', through='Feedback')

    def __str__(self):
        return self.username


class Customer(User):
    address = models.TextField(max_length=255, null=True)
    city = models.TextField(max_length=255, null=True)
    district = models.TextField(max_length=255, null=True)

    # Thiết lập mối quan hệ One To One (Customer - User)
    # user_ptr = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)

    # Thiết lập mối quan hệ Many (Customer) to Many (Shipper) thông qua bảng Feedback
    shippers = models.ManyToManyField('Shipper', through='Feedback')

    def address_full(self):
        return f'{self.address}, {self.district}, {self.city}.'

    def __str__(self):
        return self.username


# Đơn hàng khách hàng đăng
class Order(ModelBase):
    description = RichTextField()
    start_address = models.TextField(max_length=255, null=False, blank=False, default=Customer.address_full)
    end_address = models.TextField(max_length=255, null=False, blank=False)
    distance = models.FloatField(blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='orders/%Y/%m')
    weight = models.FloatField(blank=True)
    size = models.CharField(max_length=10, blank=True)
    status = models.CharField(max_length=50, null=False,
                              default="Open")  # biến để chứa tính trạng bài viết: đang đấu giá, đã đấu giá thành công
    # created_date (kế thừa)
    # updated_date (kế thừa)
    # active (kế thừa): các bài viết đã xoá

    # Thiết lập mối quan hệ Many (Order) to One (Customer)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='orders')

    # Thiết lập mối quan hệ Many (Order) to Many (Shipper) thông qua bảng Bargain
    shippers = models.ManyToManyField('Shipper', through='Bargain')

    def __str__(self):
        return self.description


# Phiếu đấu giá của shipper
class Bargain(ModelBase):
    # OrderID
    # ShipperID
    # created_date
    # updated_date
    price = models.DecimalField(max_digits=20, decimal_places=10, null=False, blank=False)
    # biến cho biết shipper đã đấu giá và giành quyền vận chuyển thành công
    is_bargained = models.BooleanField(default=False, null=False, blank=False)
    # biến cho biết shipper đã vận chuyển và xác nhận vận chuyển thành công
    is_confirmed = models.BooleanField(default=False, null=False, blank=False)

    # Thiết lập khoá ngoại
    shipper = models.ForeignKey('Shipper', on_delete=models.SET_NULL, null=True, related_name="bg_shippers")
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True, related_name="bg_orders")


class Feedback(ModelBase):
    # CustomerID
    # OrderID
    # ShipperID
    # created_date
    content = models.TextField(max_length=255, blank=True)
    rating = models.SmallIntegerField(blank=True)

    # Thiết lập khoá ngoại
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, related_name="fb_customers")
    shipper = models.ForeignKey('Shipper', on_delete=models.SET_NULL, null=True, related_name="fb_shippers")
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True, related_name="fb_orders")
