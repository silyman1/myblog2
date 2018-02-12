# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_heart'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='heart_num',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
