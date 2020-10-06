# Generated by Django 3.0.7 on 2020-09-23 02:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Category Name')),
                ('color', models.CharField(choices=[('blue', 'primary'), ('secondary', 'secondary'), ('danger', 'danger'), ('info', 'info'), ('sucesss', 'sucesss'), ('warning', 'warning')], max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True, verbose_name='To-Do Name')),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('category', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
