from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from markdownx import urls as markdownx

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls',namespace='products') ),
    path('users/', include('users.urls',namespace='users')),
    url(r'^markdownx/', include(markdownx)),
]

