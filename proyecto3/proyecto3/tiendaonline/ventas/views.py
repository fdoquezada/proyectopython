from django.shortcuts import render
from .models import Cliente
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


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