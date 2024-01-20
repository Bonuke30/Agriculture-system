# Generated by Django 5.0 on 2024-01-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('GH', 'Ghee'), ('LS', 'Lassi'), ('MS', 'Milk Shake'), ('CR', 'Curd'), ('IC', 'Ice-Cream'), ('CZ', 'Cheese'), ('PN', 'Paneer'), ('ML', 'Milk')], max_length=2),
        ),
    ]
