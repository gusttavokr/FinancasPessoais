from django.contrib import admin
from django.urls import path, include
from .views.views import (
    Index, verBalancete
)

urlpatterns = [
    # path("", views.login, name="index")
    path("", Index.as_view(), name="index"),
    path("balancete/<int:pk>/", verBalancete.as_view(), name="verBalancete"),
]
