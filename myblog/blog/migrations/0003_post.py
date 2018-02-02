# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180131_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField(null=True)),
                ('type', models.CharField(max_length=100)),
                ('post_image', models.CharField(max_length=200, null=True)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
