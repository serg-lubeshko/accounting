# Generated by Django 4.1.5 on 2023-02-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounting", "0005_basketexpenses_basket"),
    ]

    operations = [
        migrations.AlterField(
            model_name="basketexpenses",
            name="date",
            field=models.DateField(verbose_name="Дата"),
        ),
    ]