from django import forms
from datetime import date
from django.core.exceptions import ValidationError

class DespesaForm(forms.Form):
    """Formulário para criação das despesas"""

    valor = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Informe o valor da despesa:',
            'class': 'input w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm placeholder-gray-400 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm',
        }),
        label="Valor da despesa"
    )
    
    dataDebito = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm',
        }),
        label="Data de débito"
    )

    descricao = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm placeholder-gray-400 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm',
            'placeholder': 'Digite a descrição do balancete:',
        }),
        label="Descrição da débito"
    )

    def clean(self):
        cleaned_data = super().clean()
        erros = {}

        self.dataDebito = cleaned_data.get('dataDebito')

        if self.valor < 0:
            erros['valor'] = "O valor não pode ser 0 ou menor"

        if self.dataDebito and self.dataDebito < date.today():
            erros['dataDebito'] = "A data de despesa não pode ser no passado."

        if erros:
            raise ValidationError(erros)

        return cleaned_data
