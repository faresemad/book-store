from django import forms
from .models import Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'customer':
            forms.Select(attrs={'class': 'form-select'}),
            'book':
            forms.Select(attrs={'class': 'form-select'}),
            'tags':
            forms.CheckboxSelectMultiple(
                attrs={'class': 'form-check-control p-2 m-1 bg-light'}),
            'status':
            forms.Select(attrs={'class': 'form-select'}),
            'note':
            forms.Textarea(attrs={'class': 'form-control'}),
        }


class CreateNewUser(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }