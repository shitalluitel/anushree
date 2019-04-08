from django.contrib import admin

# Register your models here.
from orders.models import Order, OrderItem, Cart, CartItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'created_at', 'total', 'status',)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity',)


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'created_at',)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
