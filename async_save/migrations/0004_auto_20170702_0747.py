# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('async_save', '0003_auto_20170702_0650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadingfilemodel',
            old_name='symbols_number',
            new_name='characters',
        ),
    ]
