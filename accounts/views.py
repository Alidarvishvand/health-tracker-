from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import generics, permissions
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from .signals import create_user_profile,save_user_profile


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,'your account has been registered successfully')
            return redirect('profile')
    else:
        form = UserUpdateForm()
    return render(request, '../templates/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('profile')
            else:
                messages.error(request,'invalid username or password')
        else:
            messages.error(request, "invalid username or password")
    form = AuthenticationForm()
    return render(request,'../templates/login.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,"your profile has been updated successfully")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    contex = {
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, '../templates/profile.html', contex)

@login_required 
def logout(request):
    auth_logout(request)
    return redirect ('login')