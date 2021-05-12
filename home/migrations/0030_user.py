# Generated by Django 3.1.1 on 2021-04-06 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
