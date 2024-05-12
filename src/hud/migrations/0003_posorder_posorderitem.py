# Generated by Django 5.0.3 on 2024-05-12 19:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hud', '0002_rename_parent_group_productgroup_parent'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PosOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.SmallIntegerField(default=0)),
                ('discount_type', models.SmallIntegerField(default=0)),
                ('total', models.FloatField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PosOrderItem',
            fields=[
                ('number', models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('round_number', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('quantity', models.SmallIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=3, default=0, max_digits=9)),
                ('is_locked', models.BooleanField(default=False)),
                ('discount', models.FloatField(default=0)),
                ('discount_type', models.FloatField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('voided_by', models.SmallIntegerField(default=0)),
                ('comment', models.TextField(blank=True, null=True)),
                ('bundle', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='hud.posorder')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_items', to='hud.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
