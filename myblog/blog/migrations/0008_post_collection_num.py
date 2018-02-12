# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_img_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='collection_num',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
