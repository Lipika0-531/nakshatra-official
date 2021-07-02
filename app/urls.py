from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .api import apiViews

urlpatterns=[
    path("product/new/", apiViews.new, name="newProduct"),
    path("products/<int:id>", apiViews.show, name="showProduct"),
    path("products/edit/<int:id>/", apiViews.edit, name="editProduct"),
]
urlpatterns += [
    path("index", views.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
