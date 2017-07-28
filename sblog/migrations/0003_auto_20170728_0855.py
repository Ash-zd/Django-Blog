# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sblog', '0002_blog_imgurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='imgurl',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='images/test.jpg', upload_to='images/%Y/%m'),
        ),
    ]