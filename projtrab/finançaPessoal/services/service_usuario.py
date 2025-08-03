from ..models import Usuario
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError

class ServiceUsuario():
    @staticmethod
    def login_cpf(cpf, password):
        try:
            usuario = Usuario.objects.get(cpf=cpf)
        except ObjectDoesNotExist:
            # print("Usuário não encontrado")
            return None

        # if check_password(password, usuario.password):
        #     # print("Senha correta")
        
        if usuario.check_password(password):
            # print("Senha correta")
            return {"usuario": usuario}

        else:
            # print("Senha incorreta")
            return None
        
    @classmethod
    def cadastrar_usuario(cls, nome, username, cpf, endereco, dataNascimento, senha):
        usuario = Usuario(
            Nome=nome,
            username=username,
            cpf=cpf,
            endereco=endereco,
            dataNascimento=dataNascimento,
        )

        usuario.set_password(senha)
        # print("Senha criptografada SEBUG :", usuario.password)

        try:
            usuario.full_clean()
        except ValidationError as e:
            raise e

        usuario.save()
        return usuario
