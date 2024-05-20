# Generated by Django 5.0.3 on 2024-05-20 15:36

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hud', '0023_posorderitem_discount_sign_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posorderitem',
            name='discounted_amount',
            field=models.GeneratedField(db_persist=True, expression=models.Case(models.When(discount_type=1, then=django.db.models.expressions.CombinedExpression(django.db.models.expressions.CombinedExpression(models.F('price'), '*', models.F('quantity')), '*', django.db.models.expressions.CombinedExpression(models.F('discount'), '/', models.Value(100)))), models.When(discount_type=0, then=models.F('discount')), default=models.Value(0), output_field=models.DecimalField(decimal_places=3, default=0, max_digits=15)), output_field=models.DecimalField(decimal_places=3, default=0, max_digits=15)),
        ),
    ]
