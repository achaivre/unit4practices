# Generated by Django 4.1.5 on 2023-02-11 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Airline",
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
                ("date", models.DateField()),
                ("destination", models.TextField()),
                ("passenger", models.TextField()),
                ("bags", models.IntegerField(default=0)),
                ("firstclass", models.BooleanField(default=False)),
            ],
        ),
    ]
