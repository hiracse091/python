# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kk_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdocument',
            name='document_type',
            field=models.CharField(max_length=100, choices=[('1', 'original'), ('2', 'new')]),
            preserve_default=True,
        ),
    ]
