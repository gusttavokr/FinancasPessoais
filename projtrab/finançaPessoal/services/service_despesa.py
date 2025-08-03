from ..models import Despesa
from django.core.exceptions import ValidationError

class ServiceDespesa:
    @classmethod
    def criarDespesa(cls, balancete, valor, dataDebito, descricao):

        despesa = Despesa(
            balancete = balancete,
            valor = valor,
            dataDebito = dataDebito,
            descricao = descricao
        )

        try:
            despesa.full_clean()
        except ValidationError as e:
            raise e

        despesa.save()
        return despesa