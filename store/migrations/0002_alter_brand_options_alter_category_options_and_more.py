# Generated by Django 4.1.5 on 2023-01-31 19:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='specification',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='store_branch',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='images',
            name='created',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='images',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, editable=False, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='images',
            name='update',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='store_branch',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store_branch',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, editable=False, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store_branch',
            name='update',
            field=models.DateField(auto_now=True),
        ),
    ]
