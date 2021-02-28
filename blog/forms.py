from django.forms import ModelForm
from django import forms
from .models import Dogs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DogsForm(ModelForm):
    class Meta:
        model = Dogs
        fields = '__all__'


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя:',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль:',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля:',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email:', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }