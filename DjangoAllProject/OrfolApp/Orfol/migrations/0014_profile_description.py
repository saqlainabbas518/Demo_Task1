# Generated by Django 3.0.5 on 2020-04-23 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orfol', '0013_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]