from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user=User.objects.create_user(cd['username'],cd['email'],cd['password'])
            user.first_name=cd['first_name']
            user.last_name=cd['last_name']
            user.save()
            messages.success(request,'user registered')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username = cd['username'],password = cd['password'])
            if user is not None:
                login(request,User)
                messages.success(request,'logged in successfully')
                return redirect('home')
            else:
                messages.error(request,'user name or password is none','danger')

    else:
        form = UserLoginForm()
    return render(request,'login.html',{'form':form})


def user_logout(request):
    logout(request)
    messages.success(request,'logout_successfully')
    return redirect('home')