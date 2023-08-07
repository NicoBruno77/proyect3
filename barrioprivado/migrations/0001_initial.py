# Generated by Django 4.2.3 on 2023-07-25 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Residente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, verbose_name='Nombre y Apellido')),
                ('edad', models.IntegerField(blank=True)),
                ('direccion', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefono', models.PositiveBigIntegerField(blank=True)),
                ('dni', models.PositiveBigIntegerField(blank=True)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('N', 'No especifica')], default='N', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('codigo_sector', models.PositiveIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('telefono', models.PositiveBigIntegerField(blank=True)),
                ('sector', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='barrioprivado.sector')),
            ],
        ),
        migrations.CreateModel(
            name='Invitado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=20, verbose_name='Nombre y Apellido')),
                ('apellido', models.CharField(blank=True, max_length=50)),
                ('telefono', models.PositiveBigIntegerField(blank=True)),
                ('residente', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='barrioprivado.residente', verbose_name='Nombre del Inquilino')),
            ],
        ),
    ]