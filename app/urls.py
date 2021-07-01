from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import api

urlpatterns=[
    path("Product/new", api.new),
]
urlpatterns += [
    path("index", views.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
