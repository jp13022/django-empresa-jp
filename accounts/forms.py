from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


# Formulário de registro
class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email']


# Formulário de login
class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        # Autenticação
        user = authenticate(username=email, password=password)

        if user is None:
            raise forms.ValidationError("Email ou senha inválidos!")

        self.user = user
        return self.cleaned_data
