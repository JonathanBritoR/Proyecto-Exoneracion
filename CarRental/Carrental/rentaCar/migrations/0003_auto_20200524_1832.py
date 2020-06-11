# Generated by Django 3.0.6 on 2020-05-24 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentaCar', '0002_auto_20200523_2126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterModelOptions(
            name='inspeccion',
            options={'verbose_name': 'Inspeccion', 'verbose_name_plural': 'Inspecciones'},
        ),
        migrations.AlterModelOptions(
            name='marca',
            options={'verbose_name': 'Marca', 'verbose_name_plural': 'Marcas'},
        ),
        migrations.AlterModelOptions(
            name='modelo',
            options={'verbose_name': 'Modelo', 'verbose_name_plural': 'Modelos'},
        ),
        migrations.AlterModelOptions(
            name='rentaydevolucion',
            options={'verbose_name': 'Renta y Devolucion', 'verbose_name_plural': 'Rentas y Devoluciones'},
        ),
        migrations.AlterModelOptions(
            name='tipodecombustible',
            options={'verbose_name': 'Tipo de Combustible', 'verbose_name_plural': 'Tipos de Combustible'},
        ),
        migrations.AlterModelOptions(
            name='tipodevehiculo',
            options={'verbose_name': 'Tipo de Vehiculo', 'verbose_name_plural': 'Tipos de Vehiculos'},
        ),
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'verbose_name': 'Vehiculo', 'verbose_name_plural': 'Vehiculos'},
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='tipo_de_persona_choice',
            new_name='tipo_de_persona',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='tanda_labor_choices',
            new_name='tanda_labor',
        ),
    ]