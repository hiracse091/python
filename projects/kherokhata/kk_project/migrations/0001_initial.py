# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=100)),
                ('project_due_date', models.DateField()),
                ('project_estimatedtime', models.IntegerField()),
                ('project_descriptoin', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document_name', models.CharField(max_length=100)),
                ('document_description', models.TextField()),
                ('document_location', models.CharField(max_length=256)),
                ('document_type', models.CharField(max_length=100, choices=[(b'1', b'original'), (b'2', b'new')])),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('project_id', models.ForeignKey(to='kk_project.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('project_id', models.ForeignKey(to='kk_project.Project')),
                ('project_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectWorkArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='projectworkarea',
            name='area_id',
            field=models.ForeignKey(to='kk_project.WorkArea'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectworkarea',
            name='project_id',
            field=models.ForeignKey(to='kk_project.Project'),
            preserve_default=True,
        ),
    ]
