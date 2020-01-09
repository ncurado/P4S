# Generated by Django 3.0.2 on 2020-01-09 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=10)),
                ('timezone', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tvmaze_id', models.IntegerField()),
                ('network', models.CharField(max_length=30)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newshows.Country')),
            ],
            options={
                'verbose_name_plural': 'Networks',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('profile_id', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name_plural': 'Settings',
            },
        ),
        migrations.CreateModel(
            name='ShowType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'Show Types',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Webchannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tvmaze_id', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newshows.Country')),
            ],
            options={
                'verbose_name_plural': 'Webchannels',
            },
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tvmaze_id', models.IntegerField()),
                ('url', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('name', models.CharField(max_length=30, verbose_name='Show')),
                ('runtime', models.IntegerField(default=0)),
                ('premiere', models.DateTimeField(blank=True, default=None, null=True, verbose_name='premiered')),
                ('tvrage_id', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('thetvdb_id', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('imdb_id', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ignored', models.BooleanField(default=False, verbose_name='I')),
                ('insonarr', models.BooleanField(default=False, verbose_name='S')),
                ('genre', models.ManyToManyField(related_name='shows', to='newshows.Genre')),
                ('language', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='newshows.Language')),
                ('network', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='newshows.Network')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newshows.Status')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newshows.ShowType')),
                ('webchannel', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='newshows.Webchannel')),
            ],
            options={
                'verbose_name_plural': 'Shows',
            },
        ),
    ]
