# Generated by Django 4.1.3 on 2022-11-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_profesor_perfilmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]