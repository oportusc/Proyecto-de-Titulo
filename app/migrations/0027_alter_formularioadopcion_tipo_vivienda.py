# Generated by Django 4.0.4 on 2022-06-16 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_formularioadopcion_estado_solicitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioadopcion',
            name='tipo_vivienda',
            field=models.CharField(choices=[['Casa', 'Casa'], ['Departamento', 'Departamento']], max_length=50),
        ),
    ]
