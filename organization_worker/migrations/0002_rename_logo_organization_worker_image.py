# Generated by Django 3.2.12 on 2022-03-27 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization_worker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization_worker',
            old_name='logo',
            new_name='image',
        ),
    ]
