from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from markdownx import urls as markdownx
from django.conf import settings
from django.conf.urls.static import static

# Overriding default Error Page
handler403 = 'products.views.main_error_page'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls',namespace='products') ),
    path('users/', include('users.urls',namespace='users')),
    path("select2/", include("django_select2.urls")),
    url(r'^markdownx/', include(markdownx)),
]

# Serving dynamic files in development
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

