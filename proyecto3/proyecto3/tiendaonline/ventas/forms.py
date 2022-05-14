from django import forms
from django.db.models import fields
from django.contrib.auth.models import User

class ReclamoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField(widget= forms.EmailInput)
    telefono = forms.CharField(max_length=20)   
    mensaje = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
