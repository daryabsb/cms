# Generated by Django 5.0.3 on 2024-04-29 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_content2_alter_page_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='content',
        ),
    ]
