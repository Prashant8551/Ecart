# Generated by Django 5.0.2 on 2024-03-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0007_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='static/images'),
            preserve_default=False,
        ),
    ]
