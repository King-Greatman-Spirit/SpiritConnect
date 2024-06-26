# Generated by Django 3.2.12 on 2022-04-11 14:38

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activity', '0003_auto_20220411_1438'),
        ('organization', '0003_auto_20220325_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/gallery')),
                ('description', models.TextField(max_length=300)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image_name', models.CharField(max_length=100, null=True)),
                ('activity', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='organization', chained_model_field='organization', default=None, on_delete=django.db.models.deletion.CASCADE, to='activity.activity')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
            ],
            options={
                'verbose_name': 'gallery',
                'verbose_name_plural': 'galleries',
            },
        ),
    ]
