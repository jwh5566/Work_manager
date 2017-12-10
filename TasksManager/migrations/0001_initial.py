# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=50)),
                ('description', models.CharField(verbose_name='Description', max_length=1000)),
                ('client_name', models.CharField(verbose_name='Client name', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=50)),
                ('description', models.CharField(verbose_name='Description', max_length=1000)),
                ('time_elapsed', models.IntegerField(verbose_name='Elapsed time', blank=True, null=True, default=None)),
                ('importance', models.IntegerField(verbose_name='Importance')),
                ('project', models.ForeignKey(verbose_name='Project', blank=True, null=True, default=None, to='TasksManager.Project')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=50)),
                ('login', models.CharField(verbose_name='Login', max_length=25)),
                ('password', models.CharField(verbose_name='Password', max_length=100)),
                ('phone', models.CharField(verbose_name='Phone number', max_length=20, blank=True, null=True, default=None)),
                ('born_date', models.DateField(verbose_name='Born date', blank=True, null=True, default=None)),
                ('last_connection', models.DateTimeField(verbose_name='Date of last connection', blank=True, null=True, default=None)),
                ('email', models.EmailField(verbose_name='Email', max_length=254)),
                ('years_seniority', models.IntegerField(verbose_name='Seniority', default=0)),
                ('date_created', models.DateField(verbose_name='Date of Birthday', auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('userprofile_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='TasksManager.UserProfile')),
            ],
            bases=('TasksManager.userprofile',),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='TasksManager.UserProfile')),
                ('specialisation', models.CharField(verbose_name='Specialisation', max_length=50)),
            ],
            bases=('TasksManager.userprofile',),
        ),
        migrations.AddField(
            model_name='task',
            name='developer',
            field=models.ForeignKey(verbose_name='User', to='TasksManager.Developer'),
        ),
        migrations.AddField(
            model_name='developer',
            name='supervisor',
            field=models.ForeignKey(verbose_name='Supervisor', to='TasksManager.Supervisor'),
        ),
    ]
