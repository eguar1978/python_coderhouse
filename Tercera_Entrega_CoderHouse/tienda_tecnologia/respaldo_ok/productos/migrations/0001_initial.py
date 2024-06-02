# Generated by Django 5.0.6 on 2024-06-01 14:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Celular",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("marca", models.CharField(max_length=50)),
                ("modelo", models.CharField(max_length=50)),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
                ("descripcion", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Computadora",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("marca", models.CharField(max_length=50)),
                ("modelo", models.CharField(max_length=50)),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
                ("descripcion", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Televisor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("marca", models.CharField(max_length=50)),
                ("modelo", models.CharField(max_length=50)),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
                ("descripcion", models.TextField()),
            ],
        ),
    ]
