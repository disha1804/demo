# Generated by Django 4.2.7 on 2023-12-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demo_app", "0002_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="demo1",
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
                ("lname", models.CharField(max_length=50)),
                ("age", models.CharField(max_length=70)),
                ("gender", models.CharField(max_length=10)),
            ],
        ),
    ]
