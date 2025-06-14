# Generated by Django 4.2.21 on 2025-05-27 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Torneos", "0003_imagencarrusel_informaciontorneoanio"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="imagencarrusel",
            options={
                "ordering": ["orden"],
                "verbose_name_plural": "Imágenes de Carrusel",
            },
        ),
        migrations.AlterModelOptions(
            name="informaciontorneoanio",
            options={"verbose_name_plural": "Información de Torneo por Año"},
        ),
        migrations.RemoveField(
            model_name="torneo",
            name="imagen",
        ),
        migrations.AddField(
            model_name="torneo",
            name="descripcion",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="torneo",
            name="imagen_torneo",
            field=models.ImageField(
                blank=True, null=True, upload_to="torneos_imagenes/"
            ),
        ),
        migrations.AlterField(
            model_name="imagencarrusel",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="imagencarrusel",
            name="descripcion",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="imagencarrusel",
            name="fecha_subida",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="imagencarrusel",
            name="imagen",
            field=models.ImageField(upload_to="carrusel_imagenes/"),
        ),
        migrations.AlterField(
            model_name="imagencarrusel",
            name="orden",
            field=models.IntegerField(
                default=0, help_text="Define el orden en el carrusel"
            ),
        ),
        migrations.AlterField(
            model_name="imagencarrusel",
            name="titulo",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="informaciontorneoanio",
            name="anio",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="informaciontorneoanio",
            name="campeon",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="informaciontorneoanio",
            name="participantes_cantidad",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="informaciontorneoanio",
            name="resumen",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="informaciontorneoanio",
            name="subcampeon",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="informaciontorneoanio",
            name="torneo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="informacion_por_anio",
                to="Torneos.torneo",
            ),
        ),
        migrations.AlterField(
            model_name="torneo",
            name="nombre",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="torneo",
            name="tipo",
            field=models.CharField(
                choices=[
                    ("Copa", "Copa"),
                    ("Liga", "Liga"),
                    ("Superliga", "Superliga"),
                    ("Desafío", "Desafío"),
                    ("Internacional", "Internacional"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="torneo",
            name="ubicacion",
            field=models.CharField(max_length=100),
        ),
    ]
