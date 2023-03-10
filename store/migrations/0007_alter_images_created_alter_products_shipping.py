# Generated by Django 4.1 on 2023-02-10 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_products_shipping_alter_products_states'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='shipping',
            field=models.CharField(blank=True, choices=[(None, '--Please choose--'), ('Free', 'Free'), ('Not Free', 'Not Free'), ('on Stor pickup', 'on Stor pickup'), ('Buy 5+ get one free', 'Buy 5+ get one free'), ('let you know on checkout', 'let you know on checkout')], max_length=30, null=True),
        ),
    ]
