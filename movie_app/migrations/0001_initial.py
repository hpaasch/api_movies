# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('movie_title', models.CharField(max_length=75)),
                ('release_date', models.CharField(max_length=15)),
                ('video_release_date', models.CharField(default='', max_length=15)),
                ('imdb_url', models.CharField(max_length=300)),
                ('unknown', models.IntegerField()),
                ('action', models.IntegerField()),
                ('adventure', models.IntegerField()),
                ('animation', models.IntegerField()),
                ('children', models.IntegerField()),
                ('comedy', models.IntegerField()),
                ('crime', models.IntegerField()),
                ('documentary', models.IntegerField()),
                ('drama', models.IntegerField()),
                ('fantasy', models.IntegerField()),
                ('film_noir', models.IntegerField()),
                ('horror', models.IntegerField()),
                ('musical', models.IntegerField()),
                ('mystery', models.IntegerField()),
                ('romance', models.IntegerField()),
                ('scifi', models.IntegerField()),
                ('thriller', models.IntegerField()),
                ('war', models.IntegerField()),
                ('western', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=3, null=True)),
                ('occupation', models.CharField(max_length=15)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('timestamp', models.IntegerField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_app.Movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_app.Rater')),
            ],
        ),
    ]