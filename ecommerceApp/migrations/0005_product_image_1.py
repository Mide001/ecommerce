# Generated by Django 4.0.3 on 2022-05-06 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceApp', '0004_product_image_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_1',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
