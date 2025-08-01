from django import forms
from datetime import date, datetime
from django.core.exceptions import ValidationError

class BalanceteForm(forms.Form):
    """Formulário para criação dos balancetes"""

    nome = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'Digite o nome do balancete:',
            'class': 'w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm placeholder-gray-400 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm',
        }),
        label="Nome do balancete"
    )

    valor = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'class': 'input',
            'placeholder': 'Informe a meta de valor do balancete:',
            'class': 'w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm placeholder-gray-400 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm',
        }),
        label="Valor do balancete"
    )

    descricao = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'Digite a descrição do balancete:',
            'class': 'w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm placeholder-gray-400 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm',
        }),
        label="Descrição do balancete"
    )

    # data_criacao = forms.DateField(
    #     required=False,
    #     widget=forms.DateInput(attrs={
    #         'type': 'date',
    #         'class': 'input'
    #     }),
    #     label="Data de criação"
    # )

    def clean(self):
        cleaned_data = super().clean()
        erros = {}

        nome = cleaned_data.get('nome')
        data_criacao = cleaned_data.get('data_criacao')

        if nome and len(nome.strip()) < 3:
            erros['nome'] = "O nome deve ter pelo menos 3 caracteres."

        if data_criacao and data_criacao > date.today():
            erros['data_criacao'] = "A data de criação não pode ser no futuro."

        if erros:
            raise ValidationError(erros)

        return cleaned_data
