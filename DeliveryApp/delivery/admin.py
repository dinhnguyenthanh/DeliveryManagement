from django.contrib import admin
from django.utils.html import mark_safe

from . models import User, Category, Customer, Shipper, CategoryItem, Goods


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date']
    list_filter = ['name', 'created_date']


class CategoryItemAdmin(admin.ModelAdmin):
    search_fields = ['name', 'category']
    list_display = ['id', 'name', 'created_date']
    list_filter = ['category']
    readonly_fields = ['image_view']

    def image_view(self, item):
        if item:
            return mark_safe('<img src="/static/{url}" width="180" />'.format(url=item.image.name))


class GoodsAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name', 'created_date', 'category_item']

    readonly_fields = ['image_view']

    def image_view(self, good):
        if good:
            return mark_safe('<img src="/static/{url}" width="180" />'.format(url=good.image.name))


admin.site.register(User)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryItem, CategoryItemAdmin)
admin.site.register(Customer)
admin.site.register(Shipper)
admin.site.register(Goods, GoodsAdmin)

