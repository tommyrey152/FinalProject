# Generated by Django 5.0.4 on 2024-04-12 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0005_remove_product_size_productsize"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="size",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.DeleteModel(name="ProductSize",),
    ]