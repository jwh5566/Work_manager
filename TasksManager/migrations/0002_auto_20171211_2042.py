# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TasksManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='developer',
            field=models.ForeignKey(verbose_name='User', related_name='developers', to='TasksManager.Developer'),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(verbose_name='Project', blank=True, null=True, default=None, related_name='tasks', to='TasksManager.Project'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_elapsed',
            field=models.IntegerField(verbose_name='Elapsed time(days)', blank=True, null=True, default=None),
        ),
    ]
