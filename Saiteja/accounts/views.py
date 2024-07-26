from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, VendorProfileForm, UserProfileForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            if user.is_vendor:
                vendor_form = VendorProfileForm(request.POST, request.FILES)
                if vendor_form.is_valid():
                    vendor_profile = vendor_form.save(commit=False)
                    vendor_profile.user = user
                    vendor_profile.save()
            elif user.is_user:
                user_profile_form = UserProfileForm(request.POST)
                if user_profile_form.is_valid():
                    user_profile = user_profile_form.save(commit=False)
                    user_profile.user = user
                    user_profile.save()
            auth_login(request, user)
            return redirect('index')
    else:
        user_form = CustomUserCreationForm()
        vendor_form = VendorProfileForm()
        user_profile_form = UserProfileForm()
    return render(request, 'accounts/register.html', {
        'user_form': user_form,
        'vendor_form': vendor_form,
        'user_profile_form': user_profile_form,
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def profile(request):
    if request.user.is_vendor:
        profile = request.user.vendorprofile
    else:
        profile = request.user.userprofile
    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('index')
