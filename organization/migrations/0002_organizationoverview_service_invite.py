# Generated by Django 3.2.12 on 2022-03-25 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationoverview',
            name='service_invite',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
