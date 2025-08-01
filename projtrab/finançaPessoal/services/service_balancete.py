from ..models import Usuario, Balancete, Receita

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