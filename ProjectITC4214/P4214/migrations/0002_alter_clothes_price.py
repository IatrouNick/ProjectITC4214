# Generated by Django 4.0.3 on 2022-03-26 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('P4214', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
