from django.contrib import admin
from products.models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'size', 'stock', 'pr', 'pattern_name', 'pattern_code', 'category')
    list_filter = ['category',]
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
