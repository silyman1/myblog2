# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_comment_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
