from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['full_name', 'phone', 'img', 'email']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),

        }


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'eddition', 'publication', 'category', 'cost', 'amount', 'pages', 'language', 'img','description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'eddition': forms.TextInput(attrs={'class': 'form-control'}),
            'publication': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'pages': forms.TextInput(attrs={'class': 'form-control'}),
            'language': forms.TextInput(attrs={'class': 'form-control'}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }


class CreateReceivedForm(forms.ModelForm):
    class Meta:
        model = Received
        fields = ['reader', 'book']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'book': forms.Select(attrs={'class': 'form-control'}) }


