# Generated by Django 4.0.4 on 2022-05-02 12:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-date_added']},
        ),
        migrations.AddField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]