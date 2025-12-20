from django.contrib import admin
from .models import Category, Product, Cart, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'price', 'quantity')

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('id', 'user', 'total_amount', 'payment_method', 'created_at')

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)
