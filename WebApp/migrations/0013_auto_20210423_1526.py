# Generated by Django 3.1.4 on 2021-04-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0012_auto_20210423_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
