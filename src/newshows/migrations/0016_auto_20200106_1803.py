# Generated by Django 3.0.1 on 2020-01-06 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newshows', '0015_auto_20200103_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='setting',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='value',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
