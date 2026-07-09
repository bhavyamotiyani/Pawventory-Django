from django.urls import path
from .views import home_page, login_page, register_page, logout_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('login_page/', login_page, name='login_page'),
    path('register_page/', register_page, name='register_page'),
    path('logout_page/', logout_page, name='logout_page'),
]