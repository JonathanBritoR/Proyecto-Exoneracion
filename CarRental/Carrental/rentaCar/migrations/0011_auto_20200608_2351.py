# Generated by Django 3.0.6 on 2020-06-09 03:51

import django.core.validators
from django.db import migrations, models
import rentaCar.validations


class Migration(migrations.Migration):

    dependencies = [
        ('rentaCar', '0010_auto_20200608_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cedula',
            field=models.CharField(max_length=13, unique=True, validators=[rentaCar.validations.validar_digito_verificador, django.core.validators.RegexValidator(message='Cedula con guiones Ex:(001-0000000-1)', regex='^\\d{3}-\\d{7}-\\d$')]),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='cedula',
            field=models.CharField(max_length=13, unique=True, validators=[rentaCar.validations.validar_digito_verificador, django.core.validators.RegexValidator(message='Cedula con guiones Ex:(001-0000000-1', regex='^\\d{3}-\\d{7}-\\d$')]),
        ),
        migrations.AlterField(
            model_name='rentaydevolucion',
            name='fecha_devolucion',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
