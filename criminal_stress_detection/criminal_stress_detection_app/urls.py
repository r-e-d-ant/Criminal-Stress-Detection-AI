
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("required-data", views.required_data, name="required_data"),
    path("service", views.service, name="service")
]
