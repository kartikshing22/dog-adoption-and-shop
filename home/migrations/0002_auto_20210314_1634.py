# Generated by Django 3.1.1 on 2021-03-14 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='age',
        ),
    ]
