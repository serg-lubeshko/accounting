# Generated by Django 4.1.5 on 2023-03-06 20:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounting", "0012_alter_basketexpenses_store"),
    ]

    operations = [
        migrations.AlterField(
            model_name="basketexpenses",
            name="cost",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=8,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Стоимость",
            ),
        ),
    ]
