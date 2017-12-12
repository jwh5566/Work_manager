# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(verbose_name='Title', max_length=50)),
                ('description', models.CharField(verbose_name='Description', max_length=1000)),
                ('client_name', models.CharField(verbose_name='Client name', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(verbose_name='Title', max_length=50)),
                ('description', models.CharField(verbose_name='Description', max_length=1000)),
                ('time_elapsed', models.IntegerField(blank=True, verbose_name='Elapsed time(days)', null=True, default=None)),
                ('importance', models.IntegerField(verbose_name='Importance')),
                ('project', models.ForeignKey(blank=True, verbose_name='Project', related_name='tasks', null=True, to='TasksManager.Project', default=None)),
            ],
            options={
                'verbose_name_plural': 'tasks',
                'verbose_name': 'task',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_auth', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, primary_key=True)),
                ('phone', models.CharField(blank=True, verbose_name='Phone number', null=True, default=None, max_length=20)),
                ('born_date', models.DateField(blank=True, verbose_name='Born date', null=True, default=None)),
                ('last_connection', models.DateTimeField(blank=True, verbose_name='Date of last connection', null=True, default=None)),
                ('years_seniority', models.IntegerField(verbose_name='Seniority', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, to='TasksManager.UserProfile', serialize=False, primary_key=True, parent_link=True)),
            ],
            bases=('TasksManager.userprofile',),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, to='TasksManager.UserProfile', serialize=False, primary_key=True, parent_link=True)),
                ('specialisation', models.CharField(verbose_name='Specialisation', max_length=50)),
            ],
            bases=('TasksManager.userprofile',),
        ),
        migrations.AddField(
            model_name='task',
            name='developer',
            field=models.ForeignKey(verbose_name='User', related_name='developers', to='TasksManager.Developer'),
        ),
        migrations.AddField(
            model_name='developer',
            name='supervisor',
            field=models.ForeignKey(verbose_name='Supervisor', to='TasksManager.Supervisor'),
        ),
    ]
