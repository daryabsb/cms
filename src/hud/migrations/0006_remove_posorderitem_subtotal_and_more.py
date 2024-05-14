# Generated by Django 5.0.3 on 2024-05-14 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hud', '0005_posorderitem_subtotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posorderitem',
            name='subtotal',
        ),
        migrations.AlterField(
            model_name='posorderitem',
            name='quantity',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=9),
        ),
    ]
