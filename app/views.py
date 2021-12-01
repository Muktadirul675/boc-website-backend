from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import models
from . import forms
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import random, time, re

# External Functions

def is_a_valid_email(email):

    pattern = "\S+@\S+\.com"
    match = re.match(pattern, email)

    if match:
        return True
    

    return False

def password_allowed(password):
    if len(password) >= 6:
        return True

    return False

def make_username(username):
    username = username.split()
    username = "".join(username)

    return username

# Create your views here.

def home(request):
    cont = {}
    return render(request, 'home.html', cont)

def about(request):
    cont = {}
    return render(request, 'about.html', cont)

def contact(request):
    cont = {}
    return render(request, 'contact.html', cont)

def sign_up(request):
    if request.method == "POST":
        f_name = request.POST['first-name']
        l_name = request.POST['last-name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c-password']

        if not is_a_valid_email(email):
            messages.error(request, 'Please give a valid email address')
            return redirect("boc:sign_up")

        if not password_allowed(password):
            messages.error(request, 'The password must have 6 or more characters')
            return redirect('boc:sign_up')

        if password != c_password:
            messages.error(request, "Password didn't matched!")
            return redirect("boc:sign_up")

        new_user = User.objects.create_user(
                "username", email, password
            )
        new_user.first_name = f_name
        new_user.last_name = l_name
        new_user.save()
        maked_username = make_username(f"{new_user.first_name.lower()}{new_user.id}")
        new_user.username = maked_username
        new_user.save()

        login(request, new_user)

        return redirect("boc:home")

    return render(request, 'sign_up.html')

def sign_in(request):
    if request.method == "POST":
        name = request.POST['username']
        password = request.POST['password']
        if is_a_valid_email(name):
            saved = name
            try:
                name = User.objects.get(email=name).username
            except:
                name = saved
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect("boc:home")
        else:
            messages.error(request, 'Wrong Credentials!')
    return render(request, 'sign_in.html')

def sign_out(request):
    logout(request)

    return redirect("boc:home")

def profile(request):
    
    return render(request, 'profile.html')

