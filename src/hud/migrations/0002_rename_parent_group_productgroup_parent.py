# Generated by Django 5.0.3 on 2024-05-12 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productgroup',
            old_name='parent_group',
            new_name='parent',
        ),
    ]
