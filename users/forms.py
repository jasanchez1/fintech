from .models import Transaction
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class TransactionForm(forms.Form):
    cryptoType= forms.CharField(max_length=200)
    intention= forms.CharField(max_length=200)
    quantity= forms.IntegerField()

