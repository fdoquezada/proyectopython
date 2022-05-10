from django.contrib import admin
from ventas.models import *
# Register your models here.


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


admin.site.register(Cliente, clienteAdmin)
admin.site.register(Proveedore, proveedoresAdmin)
admin.site.register(pedido, pedidosAdmin)
admin.site.register(venta, ventasAdmin)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
