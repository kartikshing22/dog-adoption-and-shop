# Generated by Django 3.1.1 on 2021-04-09 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='age',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('AB', 'American Bully'), ('Bulldog', 'Bulldog'), ('Beagle', 'Beagle'), ('DM', 'Doberman'), ('BX', 'Boxer'), ('CC', 'chow chow'), ('GR', 'Golden Retriver'), ('GD', 'Great Dane'), ('LR', 'Labrador retriever'), ('MT', 'Mastiff'), ('PB', 'Pitbull'), ('PR', 'Pomeranian'), ('Poodle', 'Poodle'), ('PG', 'Pug'), ('Rottweiler', 'Rottweiler'), ('SB', 'Saint Bernard'), ('Stray_Dog', 'Stray Dog'), ('ST', 'Shih Tzu'), ('HK', 'Husky'), ('TT', 'Tibetan terrierle'), ('Yorkshire_Terrier', 'Yorkshire Terrier'), ('other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='city',
            field=models.CharField(choices=[('DL', 'Delhi'), ('AN', 'Andaman and Nicobar Islands'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('LA', 'Ladakh'), ('LD', 'Lakshadweep'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OD', 'Odisha'), ('PB', 'Punjab'), ('PY', 'Pondicherry'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TS', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UK', 'Uttarakhand'), ('WB', 'West Bengal')], max_length=50),
        ),
    ]
