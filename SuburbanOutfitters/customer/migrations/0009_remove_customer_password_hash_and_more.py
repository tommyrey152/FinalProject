# Generated by Django 5.0.1 on 2024-04-14 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_customer_password_hash_customer_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='password_hash',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
    ]
