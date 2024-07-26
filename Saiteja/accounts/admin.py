from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser, VendorProfile, UserProfile

# Inline admin for VendorProfile
class VendorProfileInline(admin.StackedInline):
    model = VendorProfile
    can_delete = False
    verbose_name_plural = 'Vendor Profile'
    fk_name = 'user'
    extra = 1

# Inline admin for UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'
    fk_name = 'user'
    extra = 1

# Custom User Admin
class UserAdmin(BaseUserAdmin):
    inlines = (VendorProfileInline, UserProfileInline)
    
    list_display = ('username', 'email', 'is_staff', 'is_vendor', 'is_user')
    list_filter = ('is_vendor', 'is_user', 'is_staff')
    search_fields = ('username', 'email')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Vendor Info', {'fields': ('is_vendor',)}),
        ('User Info', {'fields': ('is_user',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_vendor', 'is_user')}
        ),
    )

# Register the CustomUser model with the UserAdmin
admin.site.register(CustomUser, UserAdmin)

# Register VendorProfile and UserProfile models
admin.site.register(VendorProfile)
admin.site.register(UserProfile)

# Optionally unregister the Group model if it's not needed
admin.site.unregister(Group)
