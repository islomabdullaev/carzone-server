# Generated by Django 4.0.1 on 2022-02-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
