from ..models import Receita
from django.core.exceptions import ValidationError

class ServiceReceita:
    @classmethod
    def criarReceita(cls, balancete, valor, dataCredito, descricao):

        receita = Receita(
            balancete = balancete,
            valor = valor,
            dataCredito = dataCredito,
            descricao = descricao
        )

        try:
            receita.full_clean()
        except ValidationError as e:
            raise e

        receita.save()
        return receita