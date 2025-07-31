from django.contrib import admin
from django.urls import path, include
from .views.views_index import (ListarBalancetes)

urlpatterns = [
    # path("", views.login, name="index")
    path("", ListarBalancetes.as_view(), name="index"),
    path("balancetes/", ListarBalancetes.as_view(), name="meusBalancetes")
]
