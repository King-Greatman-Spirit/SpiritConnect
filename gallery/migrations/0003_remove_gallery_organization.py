# Generated by Django 3.2.12 on 2022-04-18 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_remove_gallery_activity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='organization',
        ),
    ]
