# Generated by Django 5.0 on 2024-01-01 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ML', 'Milk'), ('MS', 'Milk Shake'), ('CZ', 'Cheese'), ('IC', 'Ice-Cream'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('CR', 'Curd'), ('LS', 'Lassi')], max_length=2),
        ),
    ]
