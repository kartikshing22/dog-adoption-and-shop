# Generated by Django 3.2 on 2021-05-01 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_auto_20210412_2353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sub_category',
            new_name='user_name',
        ),
    ]
