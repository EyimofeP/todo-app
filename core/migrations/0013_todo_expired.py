# Generated by Django 3.0.7 on 2020-10-03 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20201002_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='expired',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
