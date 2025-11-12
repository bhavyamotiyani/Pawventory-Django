from . import views
from django.urls import path

urlpatterns = [
    path('register_page', views.register_page, name='register_page'),
    path('login_page', views.login_page, name='login_page'),
    path('home_page', views.home_page, name='home_page'),
]