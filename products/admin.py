from django.contrib import admin
from .models import Products, Product_Image
# Register your models here.

# Changing site's displayed name

admin.site.site_header = "Products Admin"
admin.site.site_title = "Products Admin Area"
admin.site.index_title = "Welcome to Products Admin Area"

class ImageInline(admin.TabularInline):
    """
    Shows Image form inside the user admin form
    """
    model = Product_Image
    can_delete = True
    verbose_name_plural = "Imagens"
    # fk_name = "products"

class CustomProductAdmin(admin.ModelAdmin):
    """
    "Overriding User admin page, to add Product_Image as an Inline"
    """
    inlines = (ImageInline, )
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomProductAdmin, self).get_inline_instances(request, obj)

# Register Model, and customModelAdmin

admin.site.register(Products, CustomProductAdmin)