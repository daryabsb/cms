# Generated by Django 5.0.3 on 2024-05-18 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hud', '0019_alter_posorderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='posorder',
            name='item_subtotal',
            field=models.FloatField(default=0),
        ),
    ]
