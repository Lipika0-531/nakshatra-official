from django.shortcuts import render
from . import models
from django.db.models import Max
# Create your views here.


def index(request):
    categories = models.Categories.objects.annotate(max_likes=Max('products__likes'))
    categories=[category.products_set.first() for category in categories]
    products = models.Products.objects.all().order_by('-id')[:9]
    context={'categories': categories, 'products':products}
    return render(request, "app/index.html", context)

