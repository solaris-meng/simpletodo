# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_id', models.CharField(default=b'tmp', max_length=256)),
                ('time_start', models.DateTimeField(null=True)),
                ('time_end', models.DateTimeField(null=True)),
                ('status', models.CharField(default=b'init', max_length=64)),
                ('content', models.TextField(default=b'tmp', max_length=1024)),
                ('new_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
