from ..models import Usuario, Balancete

class Service_Balancete:
    def listar_balancete(cls, user_id: int, ):
        usuario = Usuario.objects.get(id = user_id)

        balancetes = Balancete.objects.filter(usuario = usuario)

        return {
            'balancetes':balancetes,
            'usuario': usuario
        }