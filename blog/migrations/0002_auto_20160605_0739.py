# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('personal', 'personal'), ('designing', 'designing'), ('programming', 'programming')], max_length=50),
        ),
    ]