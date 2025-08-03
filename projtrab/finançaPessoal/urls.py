from django.contrib import admin
from django.urls import path, include
from .views.viewsBalancete import (
    Index, verBalancete, criarBalancete, 
)
from .views.viewsUsuario import(
    LoginView, LogoutView
)
from .views.viewsReceita import (
    criarReceita
)

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("paginaInicial/", Index.as_view(), name="index"),

    path("balancete/<int:pk>/", verBalancete.as_view(), name="verBalancete"),
    path("balancete/criar/", criarBalancete.as_view(), name="criarBalancete"),
    path("balancete/<int:pk>/nova-receita/", criarReceita.as_view(), name="criarReceita"),


    path("sair/", LogoutView.as_view(), name="sair")
]
