# Generated by Django 3.1.1 on 2021-04-01 17:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_delete_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
