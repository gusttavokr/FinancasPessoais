from django.shortcuts import render, redirect
from django.views import View
from ..services import service_usuario
from ..forms import formsLogin
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