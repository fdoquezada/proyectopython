from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('clientes/', views.clientes, name='clientes'),
    path('formulario/', views.formulario, name='formulario'),
    path('reclamo2/', views.reclamo2, name='reclamo2'),
    path('login/', views.login, name='login'),
   
]