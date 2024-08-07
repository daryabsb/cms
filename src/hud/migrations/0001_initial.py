# Generated by Django 5.0.3 on 2024-05-12 09:10

import django.db.models.deletion
import mptt.fields
import src.hud.modules
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(max_length=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currencies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('plu', models.IntegerField(blank=True, null=True)),
                ('measurement_unit', models.CharField(blank=True, max_length=10, null=True)),
                ('price', models.DecimalField(decimal_places=3, default=0, max_digits=11)),
                ('is_tax_inclusive_price', models.BooleanField(default=False)),
                ('is_price_change_allowed', models.BooleanField(default=False)),
                ('is_service', models.BooleanField(default=False)),
                ('is_using_default_quantity', models.BooleanField(default=True)),
                ('is_product', models.BooleanField(default=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=11, null=True)),
                ('margin', models.DecimalField(decimal_places=3, default=0, max_digits=18)),
                ('image', models.ImageField(blank=True, null=True, upload_to=src.hud.modules.upload_image_file_path)),
                ('color', models.CharField(default='Transparent', max_length=50)),
                ('is_enabled', models.BooleanField(default=True)),
                ('age_restriction', models.SmallIntegerField(blank=True, null=True)),
                ('last_purchase_price', models.DecimalField(decimal_places=3, default=0, max_digits=11)),
                ('rank', models.SmallIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='hud.currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barcodes', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barcodes', to='hud.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True)),
                ('color', models.CharField(default='Transparent', max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to=src.hud.modules.upload_image_file_path)),
                ('rank', models.SmallIntegerField(default=0)),
                ('is_product', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent_group', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groups', to='hud.productgroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productGroups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ProductGroup',
                'verbose_name_plural': 'ProductGroups',
                'ordering': ('rank',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='parent_group',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='hud.productgroup'),
        ),
    ]
