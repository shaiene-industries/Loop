from django.contrib import admin
from .models import Products
# Register your models here.
admin.site.register(Products)

# Changing site's displayed name

admin.site.site_header = "Products Admin"
admin.site.site_title = "Products Admin Area"
admin.site.index_title = "Welcome to Products Admin Area"

