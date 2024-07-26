from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, VendorProfile, UserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'is_vendor', 'is_user')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       

class VendorProfileForm(forms.ModelForm):
    class Meta:
        model = VendorProfile
        fields = ('company_name', 'website_link', 'phone_number', 'address', 'profile_image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
     

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'address', 'profile_image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

