from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
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
            return redirect('index')