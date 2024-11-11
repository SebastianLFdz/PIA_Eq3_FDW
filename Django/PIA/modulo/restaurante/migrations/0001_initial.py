# Generated by Django 5.1.2 on 2024-10-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ALUMNO",
            fields=[
                (
                    "IdAlumno",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("Matricula", models.CharField(max_length=10)),
                ("Nombre", models.CharField(max_length=80)),
                ("PrimerApellido", models.CharField(max_length=50)),
                ("SegundoApellido", models.CharField(max_length=50)),
                ("FechaNacimiento", models.DateField()),
                ("Telefono", models.CharField(max_length=15)),
                ("Correo", models.EmailField(max_length=254)),
                ("Calle", models.CharField(max_length=50)),
                ("Numero", models.CharField(max_length=5)),
                ("Colonia", models.CharField(max_length=50)),
                ("CodigoPostal", models.CharField(max_length=5)),
                ("FechaRegistro", models.DateTimeField()),
            ],
        ),
    ]
