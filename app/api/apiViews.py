from django.http.response import JsonResponse
from . import apiForms
from .. import models
from django.shortcuts import redirect, render
def new(request):
    if request.method=='POST':
        form = apiForms.NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('newProduct')
    else:
        form = apiForms.NewProductForm()
    return render(request, "app/API/products/new.html",{"form":form})


def edit(request):
    pass

def show(request):
    pass



def productDetails(request, id):
    products = models.Products.objects.filter(id=id)
    
    response ={
            "status": "Success",
            "detail":"hello"
        }
    return JsonResponse(products)
