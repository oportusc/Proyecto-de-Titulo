# Generated by Django 4.0.4 on 2022-06-16 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_formularioadopcion_estado_solicitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioadopcion',
            name='estado_solicitud',
            field=models.CharField(choices=[['Pendiente', 'Pendiente'], ['Aprobada', 'Aprobada'], ['Rechazada', 'Rechazada']], default='Pendiente', max_length=50),
        ),
    ]
