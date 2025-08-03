from django.shortcuts import render, redirect
from django.views import View
from ..services import service_usuario
from ..forms import formsLogin, formsCadastro
from django.contrib import messages

class LoginView(View):
    def get(self, request):
        """Tela de login"""
        form = formsLogin.LoginForm()
        return render(request, "login.html", {"form":form})
    
    def post(self, request):
        form = formsLogin.LoginForm()
        cpfUser = request.POST.get('cpf')
        passwordUser = request.POST.get('password')

        print("Senha recebida no login:", passwordUser)

        service = service_usuario.ServiceUsuario()
        context = service.login_cpf(cpfUser, passwordUser)

        if context is None:
            messages.error(request, "CPF e senha inválidos")
            return render(request, 'login.html', {"form":form})
        else:
            usuario = context["usuario"]  # pega o usuário do contexto
            request.session['usuario_id'] = usuario.id  # salva o id na sessão
            return redirect('index')
        
class LogoutView(View):
    def get(self, request):
        """Remove as informações do usuário da sessão."""

        request.session.flush()
        form = formsLogin.LoginForm()
        return render(request, "login.html", {"form":form})
    
class CadastroView(View):
    def get(self, request):
        """Tela de cadastro"""
        form = formsCadastro.CadastroForm()
        return render(request, "cadastro.html", {"form":form})

    def post(self, request):

        form = formsLogin.LoginForm()
        nome = request.POST.get('nome')
        username = request.POST.get('username')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        data = request.POST.get('dataNascimento')
        senha = request.POST.get('password')
        # print("Senha recebida no cadastro:", senha)

        service = service_usuario.ServiceUsuario()

        usuario = service.cadastrar_usuario(nome, username, cpf, endereco, data, senha)
        request.session['usuario_id'] = usuario.id  # salva o id na sessão
        return render(request, "login.html", {"form" : form})