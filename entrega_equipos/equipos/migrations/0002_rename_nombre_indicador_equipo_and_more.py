# Generated by Django 5.1.2 on 2024-11-06 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indicador',
            old_name='nombre',
            new_name='equipo',
        ),
        migrations.RemoveField(
            model_name='indicador',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='indicador',
            name='valor',
        ),
        migrations.AddField(
            model_name='indicador',
            name='especialidad',
            field=models.CharField(default='Especialidad', max_length=50),
        ),
        migrations.AddField(
            model_name='indicador',
            name='texto',
            field=models.CharField(default='Valor', max_length=100),
            preserve_default=False,
        ),
    ]
