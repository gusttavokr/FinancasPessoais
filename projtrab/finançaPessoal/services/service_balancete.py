from ..models import Usuario, Balancete, Receita, Despesa
from datetime import date
from django.core.exceptions import ValidationError
from django.db.models import Sum

class Service_Balancete:
    @classmethod
    def listar_balancete(cls, user_id: int):
        usuario = Usuario.objects.get(id = user_id)

        balancetes = Balancete.objects.filter(usuario = usuario)

        return {
            'balancetes':balancetes,
            'usuario': usuario
        }
    
    @classmethod
    def buscarBalancete(cls, balancete_id:int):
        balancete = Balancete.objects.get(id = balancete_id)
        receitas = Receita.objects.filter(balancete__id=balancete_id)
        despesas = Despesa.objects.filter(balancete__id=balancete_id)

        totalReceitas = float(receitas.aggregate(Sum('valor'))['valor__sum'] or 0)
        totalDespesas = float(despesas.aggregate(Sum('valor'))['valor__sum'] or 0)

        saldo = totalReceitas - totalDespesas

        totalReceitas = f"{totalReceitas:.2f}"
        totalDespesas = f"{totalDespesas:.2f}"
        saldo = f"{saldo:.2f}"

        return {
            "balancete" : balancete,
            "receitas" : receitas,
            "despesas" : despesas,
            'totalReceitas' : totalReceitas,
            'saldo' : saldo,
        }
    
    @classmethod
    def criarBalancete(cls, nome, saldo, descricao, user_id:int):
        dataCriacao = date.today()
        usuario = Usuario.objects.get(id = user_id)

        balancete = Balancete(
            usuario=usuario,
            nome=nome,
            saldo=saldo,
            dataCriacao=dataCriacao,
            descricao=descricao
        )

        try:
            balancete.full_clean()
        except ValidationError as e:
            raise e

        balancete.save()
        return balancete
