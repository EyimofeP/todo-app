# Generated by Django 3.0.7 on 2020-09-23 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(null=True, verbose_name='To-Do DEscription'),
        ),
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(choices=[('primary', 'Blue'), ('secondary', 'Dark Blue'), ('danger', 'Red'), ('info', 'Sky Blue'), ('sucesss', 'Green'), ('warning', 'Yellow')], max_length=50, null=True),
        ),
    ]
