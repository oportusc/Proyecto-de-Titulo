# Generated by Django 4.0.4 on 2022-05-14 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_especie', models.IntegerField(choices=[[0, 'Perro'], [1, 'Gato']])),
            ],
        ),
        migrations.CreateModel(
            name='Fundacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_fundacion', models.CharField(max_length=250)),
                ('direccion_fundacion', models.CharField(max_length=250)),
                ('contacto_fundacion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mascota', models.CharField(max_length=250)),
                ('edad_mascota', models.IntegerField()),
                ('sexo', models.IntegerField(choices=[[0, 'Hembra'], [1, 'Macho']])),
                ('descripcion', models.TextField()),
                ('tamaño', models.IntegerField(choices=[[0, 'Pequeño'], [1, 'Mediano'], [2, 'Grande']])),
                ('peso', models.IntegerField()),
                ('especie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.especie')),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_raza', models.IntegerField(choices=[[0, 'Kiltro'], [1, 'Mestizo'], [2, 'Poodle'], [3, 'Galgo'], [4, 'Otro']])),
            ],
        ),
        migrations.CreateModel(
            name='MascotaPerdida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mascota_perdida', models.CharField(max_length=250)),
                ('contacto_perdida', models.CharField(max_length=250)),
                ('fecha_extravio', models.DateField()),
                ('fecha_publicacion', models.DateField()),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='MascotaEncontrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mascota_encontrada', models.CharField(max_length=250)),
                ('fecha_encontrada', models.DateField()),
                ('fecha_publicacion', models.DateField()),
                ('contacto_encontrada', models.CharField(max_length=250)),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='MascotaAdopcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mascota_adopcion', models.CharField(max_length=250)),
                ('peso', models.IntegerField()),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.mascota')),
            ],
        ),
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.raza'),
        ),
        migrations.CreateModel(
            name='FormularioAdopcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=250)),
                ('apellidos', models.CharField(max_length=250)),
                ('edad', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('tipo_vivienda', models.IntegerField()),
                ('direccion', models.CharField(max_length=250)),
                ('otra_mascota', models.BooleanField()),
                ('fecha_solicitud', models.DateField()),
                ('estado_solicitud', models.IntegerField()),
                ('cantidad_mascotas', models.IntegerField()),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.mascota')),
            ],
        ),
    ]