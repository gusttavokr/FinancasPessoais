from django.shortcuts import render, redirect
from django.views import View
from ..services import service_balancete
from ..forms.formsBalancete import BalanceteForm
from django.urls import reverse

class Index(View):
    def get(self, request):

        user_id = request.session.get('usuario_id')
        if not user_id:
            return redirect('login')  # proteção se não estiver logado
        
        service = service_balancete.Service_Balancete()
        context = service.listar_balancete(user_id)
        context["form"] = BalanceteForm()
        return render(request, "index.html", context)


class criarBalancete(View):
    def post(self, request):

        user_id = request.session.get('usuario_id')
        if not user_id:
            return redirect('login')  # proteção se não estiver logado

        nome = request.POST.get("nome")
        valor = request.POST.get("valor")
        descricao = request.POST.get("descricao")

        service = service_balancete.Service_Balancete()
        balancete = service.criarBalancete(nome, valor, descricao, user_id)

        return redirect(reverse('verBalancete', kwargs={'pk': balancete.pk}))

class verBalancete(View):
    def get(self, request, pk):
        service = service_balancete.Service_Balancete()
        context = service.buscarBalancete(pk)
        return render(request, "verBalancete.html", context)