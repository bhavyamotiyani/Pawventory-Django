from django.contrib import admin
from .models import User   # or whatever model Core actually has

admin.site.register(User)
