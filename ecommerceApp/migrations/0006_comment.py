# Generated by Django 4.0.3 on 2022-05-09 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceApp', '0005_product_image_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('review', models.TextField()),
            ],
        ),
    ]
