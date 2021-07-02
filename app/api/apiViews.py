from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from . import apiForms
from .. import models
from django.shortcuts import redirect, render
from . import serializers
from rest_framework import viewsets
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


def edit(request):
    pass

def show(request):
    pass




class productsApi(APIView):

    def get(self, request, id, format=None):
        response = models.Products.objects.filter(id=id)
        serializer = serializers.ProductsSerializer(response, many=True)
        return Response(serializer.data)

