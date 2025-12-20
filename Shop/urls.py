from django.urls import path
from .views import (
    shop_page,
    shop_category,
    add_to_cart,
    cart_page,
    checkout,
    increase_quantity,
    decrease_quantity,
    remove_from_cart,
    order_success, 
)

urlpatterns = [
    path('', shop_page, name='shop_page'),
    path('category/<str:category>/', shop_category, name='shop_category'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_page, name='cart_page'),
    path('checkout/', checkout, name='checkout'),

    path('cart/increase/<int:cart_id>/', increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:cart_id>/', decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:cart_id>/', remove_from_cart, name='remove_from_cart'),
    path('order-success/', order_success, name='order_success'),
]
