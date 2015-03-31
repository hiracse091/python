# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kk_task', '0004_remove_task_task_estimatedtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(max_length=100, default='2', choices=[('1', 'on'), ('2', 'off')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.CharField(max_length=100, choices=[('1', 'original'), ('2', 'new')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tasktime',
            name='task_status',
            field=models.CharField(max_length=100, default='2'),
            preserve_default=True,
        ),
    ]
