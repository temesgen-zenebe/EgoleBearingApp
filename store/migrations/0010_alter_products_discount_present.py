# Generated by Django 5.0.1 on 2024-02-05 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_discount_products_discount_present_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discount_present',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]