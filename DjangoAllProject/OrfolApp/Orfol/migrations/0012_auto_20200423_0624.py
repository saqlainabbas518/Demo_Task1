# Generated by Django 3.0.5 on 2020-04-23 01:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Orfol', '0011_auto_20200423_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
