from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "app/index.html")
def contact(request):
    return render(request, "app/contact.html")
def work(request):
    return render(request, "app/work.html")