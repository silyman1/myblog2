# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_collection_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(default=b'', max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name=b'time_to_comment')),
                ('article', models.ForeignKey(related_name='p_comment', to='blog.Post')),
                ('commentor', models.ForeignKey(related_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
