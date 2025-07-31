from django.shortcuts import render
from django.views import View
from ..services import service_balancete
from .VAR import USER_ID

# def login(request):
#     return render(request, "login.html")

class ListarBalancetes(View):
    def get(self, request):
        user_id = USER_ID
        service = service_balancete.Service_Balancete()

        context = service.listar_balancete(user_id)
        return render(request, "meusBalancetes.html", context)