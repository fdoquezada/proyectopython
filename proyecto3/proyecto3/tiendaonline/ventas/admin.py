from django.contrib import admin
from django.urls import path
from ventas.models import *
from django.urls import path
# Register your models here.
from django.http import HttpResponse




class proveedoresAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'mail', 'telefono', 'direccion']
    search_fields = ['nombre', 'apellido', 'mail', 'telefono', 'direccion']


class pedidosAdmin(admin.ModelAdmin):
    list_filter = ['fecha',]


class ventasAdmin(admin.ModelAdmin):
    list_display = ['valor', 'stock', 'unidad']
    search_fields = ['valor', 'stock', 'unidad'] 

class ProductosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock']
    search_fields = ['nombre', 'precio', 'stock']    


admin.site.register(Cliente)
admin.site.register(pedido)
admin.site.register(venta)
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Contacto)
admin.site.register(Producto)





class ProveedorAdmin(admin.ModelAdmin):
    list_display = ["categoria", "subcategoria", "related"]
    list_display_links = ["categoria", "related"]
