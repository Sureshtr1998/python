# Generated by Django 5.1.4 on 2025-01-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StudentORM",
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
                ("name", models.CharField(max_length=80)),
                ("phoneNo", models.IntegerField()),
                ("stClass", models.IntegerField()),
                ("score", models.IntegerField()),
            ],
        ),
    ]
