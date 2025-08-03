from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date, datetime
from .utils import formatarData
# Create your models here.

# Usuários
# Balancetes
# Receitas : Entradas de dinheiro
# Despezas : Saídas de dinheiro

# Views
# - Ver saldo

class Usuario(User):
    Nome = models.CharField(max_length=500)
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    endereco = models.CharField(max_length=1000, blank=True, null=True)
    dataNascimento = models.DateField()

    def clean(self):
        erros = {}

        data_formatada = formatarData(self.dataNascimento)
        if not data_formatada:
            erros['dataNascimento'] = "Formato de data de nascimento inválido. Use AAAA-MM-DD."

        if self.dataNascimento:
            hoje = date.today()
            idade_minima = hoje.replace(year=hoje.year - 16)
            if self.dataNascimento > idade_minima:
                raise ValidationError({'dataNascimento': 'O usuário deve ter no mínimo 16 anos.'})

        if len(self.Nome) <= 4:
            erros['nome'] = "O nome deve ter mais que 4 caracteres"
        if len(self.cpf) != 11:
            erros['cpf'] = "O CPF deve ter 11 caracteres"

        if erros:
            raise ValidationError(erros)
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} - {self.Nome} - {self.cpf} - {self.endereco}'

    class Meta:
        verbose_name_plural = "Usuarios"
        verbose_name = "Usuario"
        ordering = ['Nome']

class Balancete(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='balancetes')
    nome = models.CharField(max_length=500)
    saldo = models.DecimalField(default=0, decimal_places = 2, max_digits=12)
    dataCriacao = models.DateField(default=timezone.now)
    descricao = models.TextField(blank=True, null=True)

    def clean(self):

        erros = {}
        if len(self.nome) < 3:
            erros['nome'] = "O nome deve ter mais de 3 caracteres"
        
        if (self.saldo <= 0):
            erros['saldo'] = "O balancete precisa de um valor maior que 0!"

        data_formatada = formatarData(self.dataCriacao)
        if not data_formatada:
            erros['dataCriacao'] = "Formato de data de criação inválido. Use AAAA-MM-DD."
        
        if erros:
            raise ValidationError(erros)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Balancete"
        verbose_name_plural = "Balancetes"
        ordering = ["-dataCriacao"]

    def __str__(self):
        return f"{self.nome} - {self.saldo} - {self.dataCriacao} - {self.usuario.Nome}"


class Receita(models.Model):
    balancete = models.ForeignKey(Balancete, on_delete=models.CASCADE, related_name='receitas')
    valor = models.DecimalField(default=0, decimal_places = 2, max_digits=12)
    dataCredito = models.DateField(default=timezone.now)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        ordering = ["-dataCredito"]

    def clean(self):
        erros = {}

        if (self.valor < 15):
            erros["valor"] = "O valor deve ser maior que 15"

        data_formatada = formatarData(self.dataCredito)
        if not data_formatada:
            erros['dataCredito'] = "Formato de data de crédito inválido. Use AAAA-MM-DD."
        
        if erros:
            raise ValidationError(erros)
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.balancete} - {self.valor} - {self.dataCredito} - {self.descricao}'
    
class Despesa(models.Model):
    balancete = models.ForeignKey(Balancete, on_delete=models.CASCADE, related_name='despesas')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    dataDebito = models.DateField()
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Despeza"
        verbose_name_plural = "Despezas"
        ordering = ["-dataDebito"]

    def clean(self):
        erros = {}

        if (self.valor < 15):
            erros["valor"] = "O valor deve ser maior que 15"

        data_formatada = formatarData(self.dataDebito)
        if not data_formatada:
            erros['dataDebito'] = "Formato de data de débito inválido. Use AAAA-MM-DD."
        
        if erros:
            raise ValidationError(erros)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.balancete} - {self.valor} - {self.dataDebito} - {self.descricao}'