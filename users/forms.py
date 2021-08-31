from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class SignUpForm(CustomUserCreationForm):
    
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Escolha um nome de usuário'}),
        max_length=20,
        error_messages={'unique': 'Já existe um usuário cadastrado com esse nome.'}
    )
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email'})    
    )
    password1 = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}),
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}),
        strip=False,
    )
    
    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email']
