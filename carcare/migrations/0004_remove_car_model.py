# Generated by Django 4.2.4 on 2023-08-09 11:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("carcare", "0003_car_brand"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="car",
            name="model",
        ),
    ]
