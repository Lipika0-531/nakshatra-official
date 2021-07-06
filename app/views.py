from django.shortcuts import render
from . import models
from django.db.models import Max
# Create your views here.


def index(request):
    categories = models.Categories.objects.annotate(
        max_likes=Max('products__likes'))
    categories = [category.products_set.first() for category in categories]
    products = models.Products.objects.all().order_by('-id')[:9]
    context = {'categories': categories, 'products': products}
    return render(request, "app/index.html", context)


def contact(request):
    return render(request, "app/contact.html")




def work(request, id):
    products = models.Products.objects.filter(category=id)
    data = [[], [], []]
    counter = 0
    for product in products:
        if counter == 3:
            counter = 0
        data[counter].append(product)
        counter += 1
    context = {"data": data}
    return render(request, "app/work.html", context)
