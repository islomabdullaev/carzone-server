# Generated by Django 4.0.1 on 2022-01-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_description_alter_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.IntegerField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')]),
        ),
    ]
