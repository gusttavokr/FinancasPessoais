from django import forms
from django.core.exceptions import ValidationError

class CadastroForm(forms.Form):
    """Formulário para Cadastro"""

    input_classes = 'mt-1 block w-[500px] rounded-md border border-gray-300 px-3 py-2 shadow-sm placeholder-gray-400 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'

    nome = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o seu nome:',
            'class': input_classes,
        }),
        label="Insira o seu nome completo:"
    )

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu nome de usuário',
            'class': 'mt-1 block w-[500px] rounded-md border border-gray-300 px-3 py-2 shadow-sm placeholder-gray-400 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm',
        }),
        label="Nome de usuário"
    )

    cpf = forms.CharField(
        max_length=11,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o seu CPF:',
            'class': input_classes,
        }),
        label="Insira o seu CPF:"
    )
    password = forms.CharField(
        max_length=12,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite a sua senha:',
            'class': input_classes,
        }),
        label="Insira a sua senha:"
    )

    endereco = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Rua Campos das Flores, 1819',
            'class': input_classes,
        }),
        label="Insira seu endereço:"
    )
    dataNascimento = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': input_classes,
        }),
        label="Data de nascimento:"
    )

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if nome and (len(nome) < 4 or not nome.isdigit()):
            raise ValidationError("O nome deve ter no mínimo 4 caracteres.")
        return nome

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf and (len(cpf) != 11 or not cpf.isdigit()):
            raise ValidationError("O CPF deve ter 11 dígitos numéricos.")
        return cpf

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password or confirm_password:
            if password != confirm_password:
                raise ValidationError("As senhas não coincidem.")
            if password and len(password) < 6:
                raise ValidationError("A senha deve ter pelo menos 6 caracteres.")

        return cleaned_data
