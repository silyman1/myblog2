# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image_url',
            field=models.CharField(max_length=300),
        ),
    ]
