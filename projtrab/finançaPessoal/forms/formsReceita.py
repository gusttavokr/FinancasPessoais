from django import forms
from datetime import date
from django.core.exceptions import ValidationError

class ReceitaForm(forms.Form):
    """Formulário para criação das receitas"""

    valor = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Informe o valor da receita:',
            'class': 'input w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm placeholder-gray-400 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm',
        }),
        label="Valor da receita"
    )


    dataCredito = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm',
        }),
        label="Data de crédito"
    )

    descricao = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm placeholder-gray-400 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm',
            'placeholder': 'Digite a descrição do balancete:',
        }),
        label="Descrição da receita"
    )

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
