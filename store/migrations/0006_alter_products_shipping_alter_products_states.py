# Generated by Django 4.1 on 2023-02-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_products_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='shipping',
            field=models.CharField(blank=True, choices=[(None, '--Please choose--'), ('Free', 'Free'), ('Not Free', 'Not Free'), ('on Stor pickup', 'on Stor pickup'), ('Buy 5+ get free', 'Buy 5+ get free'), ('let you know on checkout', 'let you know on checkout')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='states',
            field=models.CharField(blank=True, choices=[(None, '--Please choose--'), ('new brand', 'new brand'), ('Open box', 'Open box'), ('used', 'used'), ('like New', 'like new')], max_length=30, null=True),
        ),
    ]
