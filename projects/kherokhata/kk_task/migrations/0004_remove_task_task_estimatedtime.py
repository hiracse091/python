# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kk_task', '0003_auto_20150114_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_estimatedtime',
        ),
    ]
