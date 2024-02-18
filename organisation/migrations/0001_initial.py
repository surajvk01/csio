# Generated by Django 4.1.13 on 2024-02-17 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Harper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('police_verification', models.BooleanField(default=True)),
                ('contact', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'harper',
            },
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.CharField(max_length=200)),
                ('make', models.CharField(max_length=200)),
                ('registration_no', models.IntegerField()),
                ('use', models.CharField(max_length=200)),
                ('sticker', models.BooleanField(default=True)),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'vehicles',
            },
        ),
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('registered', models.BooleanField(default=True)),
                ('registration_no', models.IntegerField()),
                ('make', models.CharField(max_length=200)),
                ('use', models.CharField(max_length=200)),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pets',
            },
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('relation', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('occupation', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'family_members',
            },
        ),
    ]
