# Generated by Django 5.0.4 on 2024-04-13 21:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0005_alter_order_shipping_address_and_more"),
        ("customer", "0007_shippingaddress"),
    ]

    operations = [
        migrations.RenameField(
            model_name="shippingaddress", old_name="street_address", new_name="address",
        ),
        migrations.AddField(
            model_name="shippingaddress",
            name="customer",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shipping_addresses",
                to="customer.customer",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="shippingaddress",
            name="city",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="shippingaddress",
            name="state",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="shippingaddress",
            name="zipcode",
            field=models.CharField(max_length=10),
        ),
    ]