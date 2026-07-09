from django.urls import path
from .api_views import product_list_api, category_list_api

urlpatterns = [
    path('products/', product_list_api, name='api_products'),
    path('categories/', category_list_api, name='api_categories'),
]
