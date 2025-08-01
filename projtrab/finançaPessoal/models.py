from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date, datetime
# Create your models here.

# Usuários
# Balancetes
# Receitas : Entradas de dinheiro
# Despezas : Saídas de dinheiro

# Views
# - Ver saldo

class Usuario(User):
    Nome = models.CharField(max_length=500)
    # email = models.CharField(max_length=500, verbose_name="E-mail")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    endereco = models.CharField(max_length=1000, blank=True, null=True)
    dataNascimento = models.DateField()

    def clean(self):
        erros = {}

        if isinstance(self.dataNascimento, str):
            try:
                data_nasc = datetime.strptime(self.dataNascimento, "%Y-%m-%d").date()
            except ValueError:
                erros['dataNascimento'] = "Formato de data de nascimento inválido. Use AAAA-MM-DD."
                data_nasc = None
        else:
            data_nasc = self.dataNascimento
        if data_nasc and data_nasc > date.today():
            erros['dataNascimento'] = "A data de nascimento não pode ser no futuro."

        if len(self.Nome) <= 3:
            erros['nome'] = "O nome deve ter mais que 3 caracteres"
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
    saldo = models.FloatField(default=0)
    dataCriacao = models.DateField(default=timezone.now)
    descricao = models.TextField(blank=True, null=True)

    def clean(self):

        erros = {}
        if len(self.nome) < 3:
            erros['nome'] = "O nome deve ter mais de 3 caracteres"
        
        if (self.saldo <= 0):
            erros['saldo'] = "O balancete precisa de um valor maior que 0!"

        if isinstance(self.dataCriacao, str):
            try:
                data = datetime.strptime(self.dataCriacao, "%Y-%m-%d").date()
            except ValueError:
                erros['dataCriacao'] = "Formato de data de criação inválido. Use AAAA-MM-DD."
                data = None
        else:
            data = self.dataCriacao

        if data and data > date.today():
            erros['dataCriacao'] = "A data de criação não pode ser no futuro."
        
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
    valor = models.DecimalField(max_digits=10, decimal_places=2)
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

        if isinstance(self.dataCredito, str):
            try:
                data = datetime.strptime(self.dataCredito, "%Y-%m-%d").date()
            except ValueError:
                erros['dataCredito'] = "Formato de data de crédito inválido. Use AAAA-MM-DD."
                data = None
        else:
            data = self.dataCredito
        
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

        if isinstance(self.dataDebito, str):
            try:
                data = datetime.strptime(self.dataDebito, "%Y-%m-%d").date()
            except ValueError:
                erros['dataDebito'] = "Formato de data de crédito inválido. Use AAAA-MM-DD."
                data = None
        
        if erros:
            raise ValidationError(erros)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.balancete} - {self.valor} - {self.dataDebito} - {self.descricao}'