# Generated by Django 4.2.7 on 2023-12-02 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DEMO",
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
                ("fname", models.CharField(max_length=50)),
                ("age", models.CharField(max_length=50)),
                ("marks", models.CharField(max_length=100)),
            ],
        ),
    ]
