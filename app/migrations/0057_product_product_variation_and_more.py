# Generated by Django 5.0 on 2024-01-13 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0056_productvariation'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_variation',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='product_variations', to='app.productvariation'),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='app.product'),
        ),
    ]
