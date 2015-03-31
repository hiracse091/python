# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kk_task', '0002_auto_20141230_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasktime',
            name='task_status',
            field=models.CharField(default=b'2', max_length=100),
        ),
    ]
