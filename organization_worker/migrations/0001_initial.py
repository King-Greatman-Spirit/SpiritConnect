# Generated by Django 3.2.12 on 2022-03-23 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization_Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('worker_title', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=500)),
                ('logo', models.ImageField(upload_to='photos/organization_worker')),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('gender', models.CharField(choices=[(0, 'Select Gender'), ('male', 'Male'), ('female', 'Female')], default=0, max_length=10)),
                ('address_line_1', models.CharField(max_length=50)),
                ('address_line_2', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('employment_date', models.DateTimeField()),
                ('terminate_date', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_user', models.BooleanField(default=False)),
                ('is_management', models.BooleanField(default=False)),
                ('is_primary_contact', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
            ],
            options={
                'verbose_name': 'organization_worker',
                'verbose_name_plural': 'organization_workers',
            },
        ),
    ]
