from decimal import Decimal

import shortuuid
from django.core.validators import RegexValidator, MinValueValidator
from django.utils import timezone
from django.db import models



# Create your models here.
from .validations import validar_digito_verificador, validar_vehiculo_rentado


def generar_numero_renta():
    return  shortuuid.ShortUUID().random(length=7)


class TipodeVehiculo(models.Model):
    descripcion = models.CharField(max_length=30)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion


    class Meta:
        verbose_name = "Tipo de Vehiculo"
        verbose_name_plural = "Tipos de Vehiculos"





class Marca(models.Model):
    descripcion = models.CharField(max_length=30)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"



class Modelo(models.Model):
    marca = models.ForeignKey(
        'Marca',
        on_delete=models.CASCADE,
    )
    descripcion = models.CharField(max_length=30)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"


class TipodeCombustible(models.Model):
    descripcion = models.CharField(max_length=30)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Tipo de Combustible"
        verbose_name_plural = "Tipos de Combustible"


class Vehiculo(models.Model):
    descripcion = models.CharField(max_length=30)
    numero_de_chasis = models.IntegerField(validators=[MinValueValidator(1)])
    numero_de_motor = models.IntegerField(validators=[MinValueValidator(1)])
    numero_de_placa = models.IntegerField(validators=[MinValueValidator(1)])

    tipo_de_vehiculo = models.ForeignKey(
        'TipodeVehiculo',
        on_delete=models.CASCADE,
    )
    marca = models.ForeignKey(
        'Marca',
        on_delete=models.CASCADE,
    )
    modelo = models.ForeignKey(
        'Modelo',
        on_delete=models.CASCADE,
    )
    tipo_de_combustible = models.ForeignKey(
        'TipodeCombustible',
        on_delete=models.CASCADE,
    )

    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion

    imagen_vehiculo = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"



class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    cedula = models.CharField(max_length=13, unique=True, validators=[validar_digito_verificador,RegexValidator(regex=r"^\d{3}-\d{7}-\d$",message="Cedula con guiones Ex:(001-0000000-1)")])
    numero_tarjeta_de_credito = models.CharField(max_length=13)
    limite_de_credito = models.IntegerField(validators=[MinValueValidator(1),])
    tipo_de_persona_choices = [
        ('Jur', 'Juridica'),
        ('Fis', 'Fisica')
    ]

    tipo_de_persona = models.CharField(max_length=3, choices=tipo_de_persona_choices)

    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    cedula = models.CharField(max_length=13, unique=True, validators=[validar_digito_verificador,RegexValidator(regex=r"^\d{3}-\d{7}-\d$",message="Cedula con guiones Ex:(001-0000000-1)")])
    tanda_labor_choices = [
        ('Mat', 'Matutina'),
        ('Noc', 'Nocturna'),
        ('Ves', 'Vespertina')

    ]
    tanda_labor = models.CharField(max_length=3, choices=tanda_labor_choices)
    porciento_comision = models.IntegerField(validators=[MinValueValidator(1)])
    fecha_ingreso = models.DateField(default=timezone.now)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

class Inspeccion(models.Model):
    vehiculo = models.ForeignKey(
        'Vehiculo',
        on_delete=models.CASCADE,
    )

    identificador_cliente = models.ForeignKey(
        'Cliente',
        on_delete=models.CASCADE,
    )

    ralladuras = models.BooleanField(default=False)

    cantidad_combustible_choices = (
        ('25%', '1/4'),
        ('50%', '1/2'),
        ('75%', '3/4'),
        ('100%', 'Full')

    )
    cantidad_combustible = models.CharField(max_length=4, choices=cantidad_combustible_choices)

    ralladuras = models.BooleanField(default=False)

    goma_de_repuesto = models.BooleanField(default=False)

    gato = models.BooleanField(default=False)

    roturas_cristal = models.BooleanField(default=False)

    estado_gomas = models.BooleanField(default=False)

    fecha = models.DateField(default=timezone.now)

    empleado_inspeccion = models.ForeignKey(
        'Empleado',
        on_delete=models.CASCADE,
    )

    estado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Inspeccion"
        verbose_name_plural = "Inspecciones"

class RentayDevolucion(models.Model):

    #Numero_renta = models.IntegerField(unique=True, validators=[MinValueValidator(1)])
    numero_renta = models.CharField(max_length=50, default=generar_numero_renta)
    def __str__(self):
        return (self.numero_renta)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk is None:
            self.vehiculo_rentayd.estado = False
            self.vehiculo_rentayd.save()
        super(RentayDevolucion, self).save(force_insert, force_update, using, update_fields)

    empleado_rentayd = models.ForeignKey(
        'Empleado',
        on_delete=models.CASCADE,
    )
    vehiculo_rentayd = models.ForeignKey(
        'Vehiculo',
        on_delete=models.CASCADE,
        validators=[validar_vehiculo_rentado]
    )
    cliente_rentayd = models.ForeignKey(
        'Cliente',
        on_delete=models.CASCADE,
    )

    fecha_renta = models.DateTimeField(default= timezone.now)

    fecha_devolucion = models.DateTimeField(blank=True, null=True)

    monto_por_dia = models.FloatField(validators=[MinValueValidator(1),])

    cantidad_de_dias = models.IntegerField(validators=[MinValueValidator(1),])

    comentario = models.CharField(max_length=100, null=True, blank=True)

    estado = models.BooleanField(default=False)

    @property
    def total (self):
        return Decimal(self.monto_por_dia) * Decimal(self.cantidad_de_dias)



    class Meta:
        verbose_name = "Renta y Devolucion"
        verbose_name_plural = "Rentas y Devoluciones"


