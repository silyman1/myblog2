# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_message_post_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessagesCount',
            fields=[
                ('user_id', models.IntegerField(serialize=False, primary_key=True)),
                ('unread_count', models.IntegerField(default=0)),
                ('total_count', models.IntegerField(default=0)),
            ],
        ),
    ]
