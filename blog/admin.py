from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post)

# Changing site's displayed name

admin.site.site_header = "Post Admin"
admin.site.site_title = "Post Admin Area"
admin.site.index_title = "Welcome to Post Admin Area"

