# Generated by Django 3.1.1 on 2021-03-27 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_delete_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
    ]
