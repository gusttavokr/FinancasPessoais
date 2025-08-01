from django.shortcuts import render
from django.views import View
from ..services import service_balancete
from .VAR import USER_ID

# def login(request):
#     return render(request, "login.html")

class Index(View):
    def get(self, request):
        user_id = USER_ID
        service = service_balancete.Service_Balancete()

        context = service.listar_balancete(user_id)
        return render(request, "index.html", context)

class verBalancete(View):
    def get(self, request, pk):
        service = service_balancete.Service_Balancete()
        context = service.buscarBalancete(pk)
        return render(request, "verBalancete.html", context)