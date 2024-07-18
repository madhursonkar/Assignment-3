from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if request.user.is_anonymous :
        return redirect('login')
    return render(request, "index.html")


def login_(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.warning(request, "Incorrect Username or Password")
            return redirect("login")
    return render(request, "loginform.html")


def signup_(request):
    if request.method == "POST":
        username = request.POST.get("createusername")
        password = request.POST.get("createpassword")
        member_ = User.objects.create_user(username=username, password=password)
        member_.save()
        return redirect('login')
    return render(request, "signup.html")

def logoutUser(request):
    logout(request)
    return redirect('login')