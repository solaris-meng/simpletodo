# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import todo.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uploadfile', models.FileField(upload_to=todo.models.update_filename)),
                ('upload_id', models.CharField(default=b'tmp', max_length=256)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
