# Generated by Django 5.0 on 2024-01-09 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_alter_productcategory_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
