from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)

    # Avoid redefining built-in fields
    # Remove the groups and user_permissions fields
    
class VendorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    website_link = models.URLField(blank=True, null=True)  # Make optional
    phone_number = models.CharField(max_length=20)  # Adjust length if needed
    address = models.TextField()
    profile_image = models.ImageField(upload_to='vendor_profiles/', blank=True, null=True)  # Optional

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)  # Adjust length if needed
    address = models.TextField()
    profile_image = models.ImageField(upload_to='user_profiles/', blank=True, null=True)  # Optional
