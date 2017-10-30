# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20171030_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treasure',
            old_name='img',
            new_name='image',
        ),
    ]
