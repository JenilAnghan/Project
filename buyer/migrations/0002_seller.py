# Generated by Django 4.1.4 on 2023-01-03 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(max_length=150)),
                ('product_color', models.CharField(max_length=50)),
                ('selling_price', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=50)),
            ],
        ),
    ]
