# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='collection',
            field=models.ManyToManyField(related_name='collector', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
