# Generated by Django 3.1.4 on 2021-04-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0013_auto_20210423_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='blood',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
