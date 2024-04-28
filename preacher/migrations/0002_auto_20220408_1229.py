# Generated by Django 3.2.12 on 2022-04-08 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preacher',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='preacher',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
