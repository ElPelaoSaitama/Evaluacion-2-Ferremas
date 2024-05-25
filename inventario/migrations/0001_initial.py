# Generated by Django 5.0.6 on 2024-05-23 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('fecha_llegada', models.DateTimeField()),
                ('custom_id', models.CharField(blank=True, max_length=50, unique=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.marca')),
            ],
        ),
    ]