from ..models import Usuario, Balancete, Receita
from datetime import date
from django.core.exceptions import ValidationError

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
        receita = Receita.objects.filter(balancete__id=balancete_id)

        return {
            "balancete" : balancete,
            "receitas" : receita
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
