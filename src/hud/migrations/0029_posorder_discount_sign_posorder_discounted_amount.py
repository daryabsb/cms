# Generated by Django 5.0.3 on 2024-05-21 03:16

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hud', '0028_alter_posorder_discount_alter_posorder_discount_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='posorder',
            name='discount_sign',
            field=models.GeneratedField(db_persist=False, expression=models.Case(models.When(discount_type=1, then=models.Value('%')), models.When(discount_type=0, then=models.Value('$')), default=models.Value(''), output_field=models.CharField(max_length=20)), output_field=models.CharField(max_length=20)),
        ),
        migrations.AddField(
            model_name='posorder',
            name='discounted_amount',
            field=models.GeneratedField(db_persist=True, expression=models.Case(models.When(discount_type=1, then=django.db.models.expressions.CombinedExpression(models.F('item_subtotal'), '*', django.db.models.expressions.CombinedExpression(models.F('discount'), '/', models.Value(100)))), models.When(discount_type=0, then=models.F('discount')), default=models.Value(0), output_field=models.DecimalField(decimal_places=3, default=0, max_digits=15)), output_field=models.DecimalField(decimal_places=3, default=0, max_digits=15)),
        ),
    ]
