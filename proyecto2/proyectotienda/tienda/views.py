from django.shortcuts import render
from .models import Cliente

# Create your views here.
def index(request):
    return render(request, 'tienda/index.html')

def contacto(request):
    return render(request, 'tienda/contacto.html')

def clientes(request):
    cliente= Cliente.objects.all()
    return render(request, 'tienda/clientes.html', {"data":cliente})