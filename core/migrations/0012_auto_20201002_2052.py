# Generated by Django 3.0.7 on 2020-10-02 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20201001_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='end_date',
            field=models.DateField(blank=True, help_text='Optional: Type this if you want this todo to expire', null=True),
        ),
    ]
