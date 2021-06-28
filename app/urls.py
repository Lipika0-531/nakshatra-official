from django.urls import path
from . import views
urlpatterns = [
    path("lipika", views.lipika),
    path("sailesh", views.sailesh),
    path("nagu", views.nagu),
    path("arshath", views.arshath),
]
