# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-03 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acc',
            name='ISBN',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='acc',
            name='ISSN',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='acc',
            name='relatorio',
            field=models.TextField(blank=True),
        ),
    ]