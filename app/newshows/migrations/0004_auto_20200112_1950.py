# Generated by Django 3.0.2 on 2020-01-12 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newshows', '0003_setting_addmonitored'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='seasonfolders',
            field=models.BooleanField(default=True, verbose_name='Subfolders for seasons'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='addmonitored',
            field=models.BooleanField(default=True, verbose_name='Add shows as monitored to Sonnar'),
        ),
    ]