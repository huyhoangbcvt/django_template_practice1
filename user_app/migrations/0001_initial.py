# Generated by Django 4.1.2 on 2022-10-15 12:58

import datetime
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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_network', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Local account'), (1, 'Google'), (2, 'Facebook'), (3, 'Linkedin')], default=0, null=True)),
                ('birthday', models.DateField(blank=True, default=None, null=True)),
                ('phone_number', models.CharField(default=None, max_length=20, null=True)),
                ('address', models.CharField(default=None, max_length=150, null=True)),
                ('description', models.CharField(default=None, max_length=100, null=True)),
                ('website', models.URLField(default=None, max_length=256, null=True)),
                ('images', models.ImageField(default=None, null=True, upload_to='images')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'db_table': 'profile',
                'ordering': ['created_at', 'birthday'],
            },
        ),
    ]
