# Generated by Django 5.0.3 on 2024-05-21 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hud', '0040_remove_posorder_total_tax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posorder',
            name='total_tax_payer',
        ),
    ]
