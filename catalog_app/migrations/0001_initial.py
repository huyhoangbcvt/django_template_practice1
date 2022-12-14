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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(default=None, null=True, upload_to='catalogs/')),
                ('content', models.TextField(default=None, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('product_map', models.PositiveSmallIntegerField(blank=True, choices=[], default=0, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'catalog_category',
                'verbose_name_plural': 'catalog_categories',
                'db_table': 'catalog_category',
                'ordering': ['created_at', 'title'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Middleship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_title', models.CharField(default=None, max_length=255, null=True)),
                ('p_name', models.CharField(default=None, max_length=100, null=True)),
                ('p_code', models.CharField(max_length=50)),
                ('p_image', models.ImageField(default=None, null=True, upload_to='products/')),
                ('p_description', models.TextField(default=None, max_length=1000, null=True)),
                ('p_country', models.CharField(default=None, max_length=50, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('middles', models.ManyToManyField(through='catalog_app.Middleship', to='catalog_app.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'catalog_product',
                'verbose_name_plural': 'catalog_products',
                'db_table': 'catalog_product',
                'ordering': ['created_at', 'p_name'],
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='middleship',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_app.product'),
        ),
    ]
