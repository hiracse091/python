# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('kk_module', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChecklistItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('checklist_item', models.CharField(max_length=256)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_name', models.CharField(max_length=100)),
                ('task_due_date', models.DateField()),
                ('task_estimatedtime', models.IntegerField()),
                ('task_description', models.TextField()),
                ('task_type', models.CharField(max_length=100, choices=[(b'1', b'original'), (b'2', b'new')])),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('module_id', models.ForeignKey(to='kk_module.Module')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskChecklist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_checklist_name', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('task_id', models.ForeignKey(to='kk_task.Task')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('task_id', models.ForeignKey(to='kk_task.Task')),
                ('task_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Urgency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('urgency_level', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='task',
            name='task_urgency_level',
            field=models.ForeignKey(to='kk_task.Urgency'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='checklistitem',
            name='checklist_id',
            field=models.ForeignKey(to='kk_task.TaskChecklist'),
            preserve_default=True,
        ),
    ]
