from django import forms
from django.db.models import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ReclamoForm(forms.Form):
    nombre = forms.CharField(label="nombre",required=True)
    email = forms.EmailField(label="email",required=True)
    telefono = forms.CharField(max_length=20)   
    mensaje = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() 
    password1 = forms.CharField(label= 'contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'confirmar contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields }
