from django.contrib import admin
from django.utils.safestring import mark_safe

from . models import User, Category, Customer, Shipper, CategoryItem, Goods


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date']
    list_filter = ['name', 'created_date']


class CategoryItemAdmin(admin.ModelAdmin):
    search_fields = ['name', 'category']
    list_display = ['id', 'name', 'created_date']
    list_filter = ['category']
    readonly_fields = ['images']

    def images(self, item):
        if item:
            return mark_safe('<img src="/static/{url}" width="160" />'.format(url=item.image.name))


admin.site.register(User)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryItem,CategoryItemAdmin)
admin.site.register(Customer)
admin.site.register(Shipper)
admin.site.register(Goods)

