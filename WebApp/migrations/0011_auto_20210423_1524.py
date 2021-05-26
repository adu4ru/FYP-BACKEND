# Generated by Django 3.1.4 on 2021-04-23 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0010_auto_20210423_1520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donation',
            options={'verbose_name_plural': 'Donations'},
        ),
        migrations.AlterField(
            model_name='donation',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='donation',
            unique_together={('date', 'donor_id', 'request_id')},
        ),
    ]
