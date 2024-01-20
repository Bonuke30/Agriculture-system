# Generated by Django 5.0 on 2024-01-13 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0057_product_product_variation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariation',
            name='product',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_variation',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.productvariation'),
        ),
    ]
