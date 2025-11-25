from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm
from .forms import RegisterForm, LoginForm


def register_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save()  # UserCreationForm já cuida da senha
            login(request, user)
            return redirect('/')  # redireciona para a home

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            login(request, form.user)  # pegamos o usuário autenticado
            return redirect('/')

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('/login/')
