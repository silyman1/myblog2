# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_heart_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_num',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
