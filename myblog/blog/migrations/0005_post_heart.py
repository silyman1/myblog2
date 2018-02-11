# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180211_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='heart',
            field=models.ManyToManyField(related_name='heart_man', to=settings.AUTH_USER_MODEL),
        ),
    ]
