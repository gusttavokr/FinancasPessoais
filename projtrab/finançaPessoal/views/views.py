from django.shortcuts import render, redirect
from django.views import View
from ..services import service_balancete
from .VAR import USER_ID
from ..forms import BalanceteForm

class Login(View):
    def get(self, request):
        return render(request, "login.html")

class Index(View):
    def get(self, request):
        user_id = USER_ID
        service = service_balancete.Service_Balancete()
        context = service.listar_balancete(user_id)
        context["form"] = BalanceteForm()
        return render(request, "index.html", context)


class criarBalancete(View):
    def post(self, request):
        user_id = USER_ID

        nome = request.POST.get("nome")
        valor = request.POST.get("valor")
        descricao = request.POST.get("descricao")

        service = service_balancete.Service_Balancete()
        balancete = service.criarBalancete(nome, valor, descricao, user_id)

        return redirect("verBalancete", pk=balancete.pk)  


class verBalancete(View):
    def get(self, request, pk):
        service = service_balancete.Service_Balancete()
        context = service.buscarBalancete(pk)
        return render(request, "verBalancete.html", context)