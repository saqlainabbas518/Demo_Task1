# Generated by Django 3.0.5 on 2020-04-22 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Orfol', '0002_auto_20200423_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='categories',
            field=models.ForeignKey(default='Accessories', on_delete=django.db.models.deletion.CASCADE, to='Orfol.Category'),
        ),
        migrations.AlterField(
            model_name='report',
            name='subcategories',
            field=models.ForeignKey(default='Lost', on_delete=django.db.models.deletion.CASCADE, to='Orfol.Subcategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='subcategories',
            field=models.CharField(choices=[('Found', 'Found'), ('Lost', 'Lost')], default='Lost', max_length=50),
        ),
    ]
