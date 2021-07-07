from django.shortcuts import render,redirect
from django.http import HttpRequest
from . import authForm
from django.contrib.auth import authenticate, login as auth_login


def register(request):
    if request.method == "POST":
        form = authForm.Register(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = authForm.Register()
    return render(request,"app/Auth/regist.html",{"form":form})

def login(request):
    if request.method == "POST":
        form = authForm.Login(request=request, data=request.POST)
        print()
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            print(form)
            if user is not None:
                auth_login(request,user)
                return redirect("index")
    else:
        form = authForm.Login()
    return render(request,"app/Auth/regist.html",{"form":form})

