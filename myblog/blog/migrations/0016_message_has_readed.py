# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20180224_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='has_readed',
            field=models.BooleanField(default=False),
        ),
    ]
