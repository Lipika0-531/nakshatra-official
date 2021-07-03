from rest_framework.response import Response
from . import apiForms
from .. import models
from django.shortcuts import redirect, render
from . import serializers
from rest_framework.views import APIView

def new(request):
    if request.method=='POST':
        form = apiForms.NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('newProduct')
    else:
        form = apiForms.NewProductForm()
    return render(request, "app/API/products/new.html",{"form":form})


def edit(request, id):
    if id:
        product = models.Products.objects.filter(id=id).first()
    form = apiForms.NewProductForm(request.POST or None, request.FILES or None,instance=product)
    if request.POST and form.is_valid():
        form.save()
        return redirect('showAll')

    context = {"form":form, "product":product}
    return render(request, "app/API/products/edit.html",context)

def delete(request, id):
    if id:
        models.Products.objects.filter(id=id).delete()
    return redirect("showAll")

def all(request):
    products = models.Products.objects.all().order_by('category')
    data=[]
    temp=[]
    initial_category = products[0].category
    for product in products:
        if product.category != initial_category:
            data.append(temp)
            temp=[]
            initial_category = product.category
        temp.append(product)

    return render(request, "app/API/products/products.html",{"products":data})



class productsApi(APIView):

    def get(self, request, id, format=None):
        response = models.Products.objects.filter(id=id)
        serializer = serializers.ProductsSerializer(response, many=True)
        return Response(serializer.data)

