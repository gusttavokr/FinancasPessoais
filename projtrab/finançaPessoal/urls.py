from django.contrib import admin
from django.urls import path, include
from .views.views import (
    Index, verBalancete, Login, criarBalancete
)

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("balancete/<int:pk>/", verBalancete.as_view(), name="verBalancete"),
    path("login/", Login.as_view(), name="login"),
    path("balancete/criar/", criarBalancete.as_view(), name="criarBalancete"),
]
