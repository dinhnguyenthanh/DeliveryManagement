from django.contrib import admin
from .models import User, Category, Customer, Deliver, Order_list, Product, Comment, Hashtag

# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Deliver)
admin.site.register(Category)
admin.site.register(Order_list)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Hashtag)
