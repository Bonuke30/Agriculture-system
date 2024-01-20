# Generated by Django 5.0 on 2024-01-01 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ML', 'Milk'), ('CZ', 'Cheese'), ('MS', 'Milk Shake'), ('GH', 'Ghee'), ('LS', 'Lassi'), ('CR', 'Curd'), ('PN', 'Paneer'), ('IC', 'Ice-Cream')], max_length=2),
        ),
    ]
