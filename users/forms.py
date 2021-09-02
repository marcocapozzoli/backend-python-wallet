from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class SignUpForm(CustomUserCreationForm):
    
    username = forms.CharField(
        label='Usuário',
        widget=forms.TextInput(),
        max_length=20,
        error_messages={'unique': 'Já existe um usuário cadastrado com esse nome.'}
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput()    
    )
    password1 = forms.CharField(
        label='Senha',
        strip=False,
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        label='Confirme a senha',
        widget=forms.PasswordInput(),
        strip=False,
    )
    
    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email']
