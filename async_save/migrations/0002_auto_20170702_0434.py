# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('async_save', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadingfile',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='uploadingfile',
            name='percents',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='uploadingfile',
            name='size',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='uploadingfile',
            name='symbols_number',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
