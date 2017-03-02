# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 20:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170228_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('telefon', models.CharField(max_length=20)),
                ('mesaj', models.TextField()),
                ('tarih', models.DateTimeField(default=datetime.datetime(2017, 3, 1, 20, 11, 0, 471000, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='yaratilis_tarihi',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 1, 20, 11, 0, 471000, tzinfo=utc)),
        ),
    ]
