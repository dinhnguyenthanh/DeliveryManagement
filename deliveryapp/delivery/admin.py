from django.contrib import admin
from django.db.models import Count
from django.template.response import HttpResponse
from .models import User, Category, OrderList, Product, Comment, Hashtag
from django import forms
from django.utils.html import mark_safe
from django.urls import path


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username']
    list_filter = ['username']
    search_fields = ['username']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date']
    list_filter = ['name', 'created_date']
    search_fields = ['name']


class OrderListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'category']
    list_filter = ['name', 'created_date', 'category__name']
    search_fields = ['name', 'category__name']


class ProductForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ['id', 'name', 'price', 'created_date', 'active', 'orderList']
    list_filter = ['name', 'price', 'created_date']
    search_fields = ['name', 'orderList__name']
    readonly_fields = ['image']

    def image(self, product):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='200px' />"
                         .format(img_url=product.images.name, alt=product.name))


class HashtagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'active']
    list_filter = ['name']
    search_fields = ['name']


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OrderList, OrderListAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)
admin.site.register(Hashtag, HashtagAdmin)
