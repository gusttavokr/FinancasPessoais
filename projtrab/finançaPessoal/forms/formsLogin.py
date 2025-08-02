from django import forms
from datetime import date
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    """Formulário para login"""

    cpf = forms.CharField(
        max_length=11,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o seu cpf:',
            'class': "mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm placeholder-gray-400 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
        }),
        label="Insira o seu cpf:"
    )
    password = forms.CharField(
        max_length=12,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite a sua senha:',
            'class': "mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm placeholder-gray-400 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
        }),
        label="Insira a sua senha:"
    )

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf and (len(cpf) != 11 or not cpf.isdigit()):
            raise ValidationError("O CPF deve ter 11 dígitos numéricos.")
        return cpf
    
    def clean_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if not self.is_edit or password:
            if password != confirm_password:
                raise ValidationError("As senhas não coincidem.")
            
            if password and len(password) < 5:
                raise ValidationError("A senha deve ter pelo menos 6 caracteres.")
        
        return cleaned_data