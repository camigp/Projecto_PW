# Generated by Django 4.1.3 on 2022-11-22 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0003_rename_task_taskmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='apellidos')),
                ('ci', models.PositiveIntegerField(verbose_name='Carnet Identidad')),
                ('nivel_escolar', models.CharField(choices=[('1', 'Profesor'), ('2', 'Decano'), ('3', 'Vicidecano')], default='1', max_length=10, verbose_name='Categoria Docente')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=50)),
                ('objeto_estudio', models.CharField(blank=True, max_length=100)),
                ('campo_accion', models.CharField(blank=True, max_length=100)),
                ('contexto_problema', models.TextField()),
                ('aprobado', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
