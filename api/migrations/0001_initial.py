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
            name='AppAuthorization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_name', models.CharField(help_text=b'Service such as pivotal, hipchat, .. etc', max_length=20)),
                ('key', models.CharField(help_text=b'Optional, typically your API_KEY value', max_length=200, null=True, blank=True)),
                ('token', models.CharField(help_text=b'Optional, this is your token or secret', max_length=200, null=True, blank=True)),
                ('user', models.ForeignKey(related_name='authentications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_number', models.CharField(max_length=20)),
                ('status_message', models.CharField(help_text=b'Twitter style status message', max_length=144, null=True, blank=True)),
                ('bio', models.TextField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_name', models.CharField(help_text=b'Describes a role that this user has', max_length=20, choices=[(b'Director', b'Director'), (b'Administrator', b'Administrator'), (b'Developer', b'Developer'), (b'Employee', b'Employee')])),
                ('user', models.ManyToManyField(related_name='roles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
