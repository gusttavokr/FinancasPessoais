from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import *

# Create your models here.

# Balancetes
# Receitas : Entradas de dinheiro
# Despezas : Saídas de dinheiro
# Usuários

# Views
# - Ver saldo

class Usuario(User):
    Nome = models.CharField(max_length=500)
    # email = models.CharField(max_length=500, verbose_name="E-mail")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    endereco = models.CharField(max_length=1000, blank=True, null=True)

    def clean(self):
         
        erros = {}
        
        if len(self.Nome) == 0:
            erros['nome'] = "O nome não pode estar vazio"
        if len(self.cpf) != 11:
            erros['cpf'] = "O CPF deve ter 11 caracteres"

        if erros:
            raise ValidationError(erros)
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Nome

    class Meta:
        verbose_name_plural = "Usuarios"
        verbose_name = "Usuario"
        ordering = ['Nome']

# class Balancete(models.Model):

#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='balancetes')
#     nome = models.CharField(max_length=500, unique=True)
#     data = date.today()

#     class Meta:
#         verbose_name = "Balancete"
#         verboce_plural_name = "Balancetes"
#         ordering = ["data"]

# class Receita(models.Model):
#     valor = models.Field