from django.contrib import admin
from django.urls import path
from ventas.models import *
from django.urls import path
# Register your models here.
from django.http import HttpResponse


class clienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'direccion')
    search_fields = ('nombre', 'apellido', 'email', )


class proveedoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'mail', 'telefono', 'direccion')
    search_fields = ('nombre', 'apellido', 'mail', )


class pedidosAdmin(admin.ModelAdmin):
    list_filter = ('fecha',)


class ventasAdmin(admin.ModelAdmin):
    list_display = ('valor', 'stock', 'unidad')
    search_fields = ('valor', 'stock', 'unidad')


admin.site.register(Cliente)
admin.site.register(pedido)
admin.site.register(venta)
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Contacto)



class ProveedorAdmin(admin.ModelAdmin):
    list_display = ["categoria", "subcategoria", "related"]
    list_display_links = ["categoria", "related"]
