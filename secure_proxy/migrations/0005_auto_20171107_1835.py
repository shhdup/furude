# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 18:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secure_proxy', '0004_auto_20171107_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cacher',
            name='content',
        ),
        migrations.RemoveField(
            model_name='cacher',
            name='force_update',
        ),
        migrations.RemoveField(
            model_name='cacher',
            name='last_updated',
        ),
        migrations.RemoveField(
            model_name='cacher',
            name='status',
        ),
        migrations.RemoveField(
            model_name='cacher',
            name='status_comment',
        ),
    ]
