# Generated by Django 2.2.5 on 2019-11-15 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('latitud', models.DecimalField(decimal_places=10, max_digits=20)),
                ('longitud', models.DecimalField(decimal_places=10, max_digits=20)),
                ('telefono', models.BigIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoDePago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('latitud', models.DecimalField(decimal_places=10, max_digits=20)),
                ('longitud', models.DecimalField(decimal_places=10, max_digits=20)),
                ('telefono', models.BigIntegerField()),
                ('descripcionNegocio', models.CharField(max_length=200)),
                ('calificacion', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maxproductos.Proveedor')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maxproductos.TipoProducto')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmado', models.BooleanField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('latitud', models.DecimalField(decimal_places=10, max_digits=20)),
                ('longitud', models.DecimalField(decimal_places=10, max_digits=20)),
                ('entregado', models.BooleanField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maxproductos.Cliente')),
                ('productos', models.ManyToManyField(to='maxproductos.Producto')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maxproductos.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaInicio', models.IntegerField()),
                ('horaFinal', models.IntegerField()),
                ('dia', models.CharField(max_length=15)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maxproductos.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
