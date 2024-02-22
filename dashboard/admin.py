from django.contrib import admin
from .models import Product, Order, Category, Customer, Supplier
from django.contrib.auth.models import Group

admin.site.site_header = 'MilingInvertory Admin'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity',)
    list_filter = ['category']

admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order),
admin.site.register(Customer),

#admin.site.unregister(Group)

