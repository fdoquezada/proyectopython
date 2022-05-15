from multiprocessing import context
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from .models import Cliente
from .forms import ReclamoForm,LoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate,  login as auth_login
from django.contrib.auth.decorators import login_required, permission_required
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'ventas/index.html')

def contacto(request):
    return render(request, 'ventas/contacto.html')


def formulario(request):
    return render(request, 'ventas/formulario.html')



def clientes(request):
    usuario= Cliente.objects.all()
    return render(request, 'ventas/clientes.html', {"data":usuario})

def reclamo2(request):
    formulario_conatacto=ReclamoForm()
    return render(request, 'ventas/reclamo2.html', {'formulario_conatacto':formulario_conatacto})


@csrf_exempt
def login(request):
    if request.method == "POST":
        form = LoginForm(data =request.POST)

        if form.is_valid():
            usuario=request.POST["nombre"]
            clave=request.POST["password"]
            user = authenticate(request, username=usuario, password=clave)
            if user is not None:

                auth_login(request, user)

        return render(request,'ventas/bienvenido.html/', {"user": user})
    else:
        form = LoginForm()
        return render(request, 'ventas/login.html', {"form": form})  


    
@login_required
def bienvenido (request):
    return render (request, 'ventas/bienvenido.html')
       
def salir(request):
    logout(request)
    return redirect ("/login")



def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usermane = form.cleaned_data['username']
            messages.success(request, f'Usuario {usermane} creado correctamente')
            return redirect('login')
    else:
        form = UserRegisterForm()     
        return render(request, 'ventas/register.html', {'form': form})
# def profile(request):           
#         return reder(request, 'ventas/profile.html', context)


















