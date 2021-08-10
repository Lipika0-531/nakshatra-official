from django.shortcuts import render,redirect
from django.http import HttpRequest
from . import authForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def register(request):
    if request.method == "POST":
        registform = authForm.Register(request.POST, prefix="regist")  
        if registform.is_valid():
            registform.save()
            return redirect("login")
    else:
         registform = authForm.Register(prefix="regist")
    
    if request.method == "POST" and not registform.is_valid():
        loginform = authForm.Login(request=request, data=request.POST, prefix="login")
        if loginform.is_valid():
            username = loginform.cleaned_data["username"]
            password = loginform.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("index")
    else:
        loginform = authForm.Login(prefix="login")
    return render(request,"app/Auth/login.html",{"registform":registform, "loginform":loginform})


def logout(request):
    auth_logout(request=request)
    return redirect("login")


def reset_1(request):
    return render(request, 'app/Auth/reset-1.html')

def reset_2(request):
    return render(request, 'app/Auth/reset-2.html')

def reset_3(request):
    return render(request, 'app/Auth/reset-3.html')