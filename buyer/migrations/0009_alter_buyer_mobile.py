# Generated by Django 4.1.4 on 2023-01-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0008_alter_buyer_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='mobile',
            field=models.CharField(max_length=15),
        ),
    ]
