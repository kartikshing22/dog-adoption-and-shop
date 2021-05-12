# Generated by Django 3.1.1 on 2021-04-12 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_auto_20210409_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(default='+91', max_length=13),
        ),
        migrations.AlterField(
            model_name='product',
            name='phone_number',
            field=models.IntegerField(default='+91', max_length=13),
        ),
    ]
