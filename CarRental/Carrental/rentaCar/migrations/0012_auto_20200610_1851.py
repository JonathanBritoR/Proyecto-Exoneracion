# Generated by Django 3.0.6 on 2020-06-10 22:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentaCar', '0011_auto_20200608_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='limite_de_credito',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='porciento_comision',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='rentaydevolucion',
            name='Numero_renta',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='rentaydevolucion',
            name='cantidad_de_dias',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='rentaydevolucion',
            name='monto_por_dia',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='numero_de_chasis',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='numero_de_motor',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='numero_de_placa',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
