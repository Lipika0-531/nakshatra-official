from django.shortcuts import render,redirect
from django.http import HttpRequest
from . import authForm
from django.contrib.auth import authenticate, login as auth_login


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


