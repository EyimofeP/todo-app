# Generated by Django 3.0.7 on 2020-09-30 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200929_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
