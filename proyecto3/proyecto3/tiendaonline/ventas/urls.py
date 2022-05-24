from django.urls import path, include
from . import views 
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('clientes/', views.clientes, name='clientes'),
    path('formulario/', views.formulario, name='formulario'),
    path('reclamo2/', views.reclamo2, name='reclamo2'),
    path('login/', views.login, name='login'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
  
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='ventas/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='ventas/logout.html'), name='logout'),
    path('agregar/', views.agregarProducto),
    path('editar/', views.editarProducto),
    path('eliminar/', views.eliminarProducto),
    path('listar/', views.listarProductos),
   
]