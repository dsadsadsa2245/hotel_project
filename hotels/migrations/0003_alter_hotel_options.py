# Generated by Django 4.2.2 on 2023-06-27 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotel',
            options={'permissions': [('change_hotel_custom', 'Can change hotel (custom)')]},
        ),
    ]