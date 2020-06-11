

# Register your models here.
from django.contrib import admin
from django.template.defaultfilters import floatformat
from django.urls import reverse
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import TipodeVehiculo, Cliente, TipodeCombustible, Marca, Modelo, Vehiculo, Empleado, Inspeccion, RentayDevolucion

class MarcaResource(resources.ModelResource):
    class Meta:
        model = Marca
#admin.site.register(Marca)
@admin.register((Marca))
class MarcaAdmin (ImportExportModelAdmin):
    list_display = ('descripcion','estado')
    resource_class = MarcaResource


#admin.site.register(TipodeCombustible)
@admin.register((TipodeCombustible))
class TipodeCombustibleAdmin (admin.ModelAdmin):
    list_display = ('descripcion','estado')

#admin.site.register(TipodeVehiculo)
@admin.register((TipodeVehiculo))
class TipodeVehiculoAdmin (admin.ModelAdmin):
    list_display = ('descripcion','estado')

class ClienteResource(resources.ModelResource):
    class Meta:
        Model = Marca
#admin.site.register(Cliente)
@admin.register(Cliente)
class ClienteAdmin (ImportExportModelAdmin):
    search_fields = ('nombre','cedula')
    list_filter = ('tipo_de_persona',)
    list_display = ('nombre','cedula','tipo_de_persona')

#admin.site.register(Modelo)
@admin.register(Modelo)
class ModeloAdmin (admin.ModelAdmin):
    list_display = ('marca','descripcion','estado')

class VehiculoResource(resources.ModelResource):
    class Meta:
        Model = Vehiculo
#admin.site.register(Vehiculo)
@admin.register(Vehiculo)
class VehiculoAdmin (ImportExportModelAdmin):
    list_display = ('descripcion','numero_de_chasis','numero_de_motor', 'marca','imagen_vehiculo', 'modelo','estado',)
    readonly_fields = ('estado',)
class EmpleadoResource(admin.ModelAdmin):
    class Meta:
        Model = Empleado
#admin.site.register(Empleado)
@admin.register(Empleado)
class EmpleadoAdmin (ImportExportModelAdmin):
    list_display = ('nombre','cedula','tanda_labor','porciento_comision','fecha_ingreso','estado')

class InspeccionResource(resources.ModelResource):
    class Meta:
        Model = Inspeccion
#admin.site.register(Inspeccion)
@admin.register(Inspeccion)
class InspeccionAdmin (ImportExportModelAdmin):
    list_display = ('vehiculo','ralladuras','cantidad_combustible','goma_de_repuesto','gato','roturas_cristal','estado_gomas','fecha','estado')

class RentayDevolucionResource(resources.ModelResource):
    class Meta:
        Model = RentayDevolucion
#admin.site.register(RentayDevolucion)
@admin.register(RentayDevolucion)
class RentayDevolucionAdmin (ImportExportModelAdmin):
    list_display = ('numero_renta','empleado_rentayd','vehiculo_rentayd','fecha_renta','fecha_devolucion','devolver',
                    'cliente_rentayd','estado','format_total')
    readonly_fields = ('numero_renta','fecha_devolucion','estado')
    def format_total (self,obj):
        return floatformat(obj.total,2)
    format_total.short_description = "total"
    def devolver (self, object):
        url_devolucion = reverse("devolver",kwargs={"id_renta":object.id})
        return format_html('<a class ="button" href="{}">Devolver</a>',url_devolucion)

admin.site.site_header = 'RentaCar'