from rest_framework.response import Response
from . import apiForms
from .. import models
from django.shortcuts import redirect, render
from . import serializers
from rest_framework.views import APIView
from rest_framework import status

def new(request):
    if request.method=='POST':
        form = apiForms.NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            user = models.User.objects.get(email=request.user)
            formobj=form.save(commit=False)
            formobj.user = user
            form.save()
            return redirect('showAll')
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
    data,temp=[],[]
    initial_category = products[0].category
    for product in products:
        if product.category != initial_category:
            data.append(temp)
            temp=[]
            initial_category = product.category
        temp.append(product)
    data.append(temp)
  
    return render(request, "app/API/products/products.html",{"products":data})



class productsApi(APIView):

    def get(self, request, id, format=None):
        response = models.Products.objects.filter(id=id)
        serializer = serializers.ProductsSerializer(response, many=True)
        return Response(serializer.data)

    # def put(self, request, id, format=None):
    #     print(request.data)
    #     user = models.User.objects.get(email='rithin36@gmail.com')

    #     product = models.Products.objects.get(id=id)
    #     rating= request.data['rating']
    #     body = request.data['body']

    #     serializer = serializers.ReviewSerializer(data={'user':user,'product':product,'rating':rating,'body':body})
    #     print(serializer.is_valid(),serializer.errors)


    #     return Response({"success":True})

# class ContentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Content
#         fields = ('title', 'body', 'topic')

#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         response['topic'] = TopicSerializer(instance.topic).data
#         return response