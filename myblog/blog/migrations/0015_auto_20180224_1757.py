# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20180224_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ManyToManyField(related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
    ]
