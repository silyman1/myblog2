# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_message_has_readed'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='post_id',
            field=models.IntegerField(null=True),
        ),
    ]
