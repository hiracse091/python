# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kk_task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('starttime', models.DateTimeField(auto_now_add=True)),
                ('endtime', models.DateTimeField(auto_now=True)),
                ('task_status', models.CharField(max_length=1, null=True)),
                ('task_id', models.ForeignKey(to='kk_task.Task')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='task',
            name='task_status',
            field=models.CharField(default=b'2', max_length=100, choices=[(b'1', b'on'), (b'2', b'off')]),
            preserve_default=True,
        ),
    ]
