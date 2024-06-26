# Generated by Django 5.0.4 on 2024-04-12 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0004_product_description_product_gender_product_image_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="size",),
        migrations.CreateModel(
            name="ProductSize",
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
                ("size", models.CharField(max_length=10)),
                ("quantity", models.IntegerField(default=0)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sizes",
                        to="customer.product",
                    ),
                ),
            ],
        ),
    ]
