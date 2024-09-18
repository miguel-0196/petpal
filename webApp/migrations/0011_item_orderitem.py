# Generated by Django 4.2 on 2023-12-18 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("webApp", "0010_alter_pet_gender_alter_pet_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="item",
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
                ("name", models.CharField(max_length=20)),
                ("price", models.IntegerField(blank=True)),
                ("description", models.TextField(blank=True, max_length=150)),
                (
                    "img",
                    models.ImageField(
                        blank=True, null=True, upload_to="webApp/static/database/"
                    ),
                ),
                ("category", models.CharField(blank=True, default="", max_length=20)),
                ("size", models.CharField(blank=True, default="", max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="orderItem",
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
                ("ordered", models.BooleanField(blank=True, default=False)),
                ("quantity", models.IntegerField(default=1)),
                (
                    "item",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webApp.item",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order",
                        to="webApp.client",
                    ),
                ),
            ],
        ),
    ]
