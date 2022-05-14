from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Cliente
from .forms import ReclamoForm,LoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate,  login as auth_login
from django.contrib.auth.decorators import login_required, permission_required


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
    if request.method == 'POST':    
        form=ReclamoForm(data= request.POST)
        nombre= form["nombre"]
        email= form["email"]
        telefono= form["telefono"]
        mensaje= form["mensaje"]
        return render(request, 'ventas/reclamo2.html', {"respuesta":"mensaje enviado"})
    else:
        form = ReclamoForm()
        return render(request, 'ventas/reclamo2.html', {"form": form})

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