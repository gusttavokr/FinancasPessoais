from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from ..services import service_usuario
from django.contrib import messages


class LoginView(View):
    def get(self, request):
        """Tela de login"""
        return render(request, "login.html")
    
    def post(self, request):
        cpfUser = request.POST.get('cpf')
        passwordUser = request.POST.get('password')

        service = service_usuario.ServiceUsuario()
        context = service.login_cpf(cpfUser, passwordUser)

        if context is None:
            messages.error(request, "CPF ou senha inválidos")
            return render(request, 'login.html')
        else:
            return redirect('index')