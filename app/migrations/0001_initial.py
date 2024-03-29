# Generated by Django 5.0.2 on 2024-02-28 01:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('simple', 'Simple'), ('doble', 'Doble'), ('matrimonial', 'Matrimonial')], max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=20)),
                ('nro_pasaporte', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=100)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('montoPagado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('formaPago', models.CharField(choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta'), ('transferencia', 'Transferencia')], max_length=100)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('pagado', 'Pagado'), ('eliminado', 'Eliminado')], max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.cliente')),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.habitacion')),
            ],
        ),
    ]
