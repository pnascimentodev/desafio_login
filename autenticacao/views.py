from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            usuario = Usuario.objects.get(email=email)
            if usuario.senha == senha:
                return redirect('menu')
            else:
                messages.error(request, 'Senha inválida')
        except Usuario.DoesNotExist:
            messages.error(request, 'E-mail inexistente')
    return render(request, 'autenticacao/login.html')

def registrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem')
        else:
            if Usuario.objects.filter(email=email).exists():
                messages.error(request, 'Este e-mail já está cadastrado.')
            else:
                Usuario.objects.create(nome=nome, email=email, senha=senha)
                messages.success(request, 'Registro realizado com sucesso!')
                return redirect('login')
    return render(request, 'autenticacao/registrar.html')

def menu(request):
    return render(request, 'autenticacao/menu.html')
