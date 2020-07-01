from django.contrib import admin
from .models import *
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'telefono']
    list_display_links = ['rut', 'nombre', 'telefono']
    search_fields = ['rut', 'nombre', 'telefono']

#class ProveedorInline(admin.StackedInline):
    #model = Proveedor

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fieldsets = (
        ('Descripcion', {
            'fields':('categoria','nombre', 'proveedor',)
        }),
        ('Variables', {
            'fields':('precio','stock',)
        }),
    )
    #inlines = [ProveedorInline]

class ProductoInline(admin.TabularInline):
    model = Producto

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre','web',)
    list_display_links = ('nombre',)
    list_filter = ('nombre','rut',)
    inlines = [ProductoInline,]

class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente','fecha', 'isDescuento')
    list_display_links = ('fecha', 'cliente')

    actions = ['aplicarDescuento', 'quitarDescuento']

    def aplicarDescuento(self, request, queryset):
        queryset.update(descuento = True)
    aplicarDescuento.short_description = 'Aplicar Descuento'

    def quitarDescuento(self, request, queryset):
        queryset.update(descuento = False)
    quitarDescuento.short_description = 'Quitar Descuento'
    

admin.site.register(Categoria)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Detalle)