from django.shortcuts import render, redirect
from django.views import View
from ..services import service_receita, service_balancete
from ..forms import formsReceita

class criarReceita(View):
    def get(self, request, pk):
        serviceBalancete = service_balancete.Service_Balancete()
        balancete_dict = serviceBalancete.buscarBalancete(pk)
        balancete = balancete_dict.get('balancete')

        context = {
            'balancete': balancete,
            'form': formsReceita.ReceitaForm()
        }
        return render(request, "receita.html", context)



    def post(self, request, pk):
        serviceBalancete = service_balancete.Service_Balancete()
        balancete_dict = serviceBalancete.buscarBalancete(pk)
        balancete = balancete_dict["balancete"]


        valor = request.POST.get('valor')
        dataCredito = request.POST.get('dataCredito')
        descricao = request.POST.get('descricao')

        service = service_receita.ServiceReceita()
        receita = service.criarReceita(balancete, valor, dataCredito, descricao)

        return redirect("verBalancete", pk=balancete.pk)
