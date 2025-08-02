from ..models import Usuario
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist

class ServiceUsuario():
    @staticmethod
    def login_cpf(cpf, password):
        try:
            usuario = Usuario.objects.get(cpf=cpf)
        except ObjectDoesNotExist:
            print("Usuário não encontrado")
            return None

        if check_password(password, usuario.password):
            print("Senha correta")
            return {"usuario": usuario}
        else:
            print("Senha incorreta")
            return None