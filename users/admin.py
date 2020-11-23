from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
from .models import Profile

class ProfileInline(admin.TabularInline):
    """
    Shows profile form inside the user admin form
    """
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"
    fk_name = "user"

class CustomUserAdmin(UserAdmin):
    """
    "Overriding User admin page, to add profile as an Inline"
    """
    inlines = (ProfileInline, )
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)