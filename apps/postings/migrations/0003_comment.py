# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-15 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0002_post_user_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_number', models.IntegerField()),
                ('message', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]