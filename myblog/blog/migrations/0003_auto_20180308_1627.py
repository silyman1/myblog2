# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180308_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
