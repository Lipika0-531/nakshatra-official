from django.urls import path

from . import views
urlpatterns = [
    path("index", views.index),
    path("contact",views.contact),
    path("work",views.work)
]
