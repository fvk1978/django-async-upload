# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('async_save', '0002_auto_20170702_0434'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadingFileModel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('size', models.IntegerField(null=True)),
                ('percents', models.IntegerField(null=True)),
                ('symbols_number', models.IntegerField(null=True)),
                ('ready', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='UploadingFile',
        ),
    ]
