# Generated by Django 5.0.2 on 2024-03-06 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0006_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
