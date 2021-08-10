from django.urls import path

from . import views
from .api import apiViews
from .auth import authViews


urlpatterns = [
    # CRUD
    path("product/new/", apiViews.new, name="newProduct"),
    path("products/<int:id>", apiViews.delete, name="deleteProduct"),
    path("products/edit/<int:id>/", apiViews.edit, name="editProduct"),
    path("products/", apiViews.all, name="showAll"),

    # API
    path("api/product/<int:id>",
         apiViews.productsApi.as_view(), name="productDetails"),


    # AUTH
    path("registration", authViews.register, name="login"),
    path("logout", authViews.logout),
    path("reset-1",authViews.reset_1),
    path("reset-2",authViews.reset_2),
    path("reset-3",authViews.reset_3),
]

urlpatterns += [
    path("index", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("work/<int:id>", views.work),
    path("profile", views.profile),
    path("like",views.like),
]
