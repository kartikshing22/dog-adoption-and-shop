# Generated by Django 3.1.1 on 2021-04-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_auto_20210409_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('American_Bully', 'American Bully'), ('Bulldog', 'Bulldog'), ('Beagle', 'Beagle'), ('Doberman', 'Doberman'), ('Boxer', 'Boxer'), ('Chow_Chow', 'chow chow'), ('Golden_Retriver', 'Golden Retriver'), ('Gret_Dane', 'Great Dane'), ('Labrador_Retriver', 'Labrador retriever'), ('Mastiff', 'Mastiff'), ('Pitbull', 'Pitbull'), ('Pomernian', 'Pomeranian'), ('Poodle', 'Poodle'), ('Pug', 'Pug'), ('Rottweiler', 'Rottweiler'), ('Saint_Benard', 'Saint Bernard'), ('Stray_Dog', 'Stray Dog'), ('Shih_Tzu', 'Shih Tzu'), ('Husky', 'Husky'), ('Tibetan_Terriele', 'Tibetan terrierle'), ('Yorkshire_Terrier', 'Yorkshire Terrier'), ('other', 'Other')], max_length=50),
        ),
    ]
