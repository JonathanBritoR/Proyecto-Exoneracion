# Generated by Django 3.0.6 on 2020-06-09 03:09

from django.db import migrations, models
import rentaCar.validations


class Migration(migrations.Migration):

    dependencies = [
        ('rentaCar', '0007_auto_20200527_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cedula',
            field=models.CharField(max_length=13, unique=True, validators=[rentaCar.validations.validar_digito_verificador, rentaCar.validations.validar_numeros_cedula, rentaCar.validations.validar_longitud_cedula]),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='cedula',
            field=models.CharField(max_length=13, unique=True, validators=[rentaCar.validations.validar_digito_verificador, rentaCar.validations.validar_numeros_cedula, rentaCar.validations.validar_longitud_cedula]),
        ),
    ]
