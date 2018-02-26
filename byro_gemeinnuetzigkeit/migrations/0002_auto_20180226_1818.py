# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-26 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('byro_gemeinnuetzigkeit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gemeinnuetzigkeitconfiguration',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Unterschriftsort'),
        ),
        migrations.AddField(
            model_name='gemeinnuetzigkeitconfiguration',
            name='veranlagungszeitraum',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Veranlagungszeitraum, z.B. 2016'),
        ),
        migrations.AlterField(
            model_name='gemeinnuetzigkeitconfiguration',
            name='reason',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Förderungszwecke, Genitiv ("zur Förderung …"), z.B. "der Bildung, sowie der Anarchie"'),
        ),
    ]
