from django.urls import path
from . import views
from django.urls.conf import include

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('clientes/', views.clientes, name='clientes'),

]
