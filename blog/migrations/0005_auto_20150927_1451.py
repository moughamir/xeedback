# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150927_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.FileField(null=True, upload_to=b'posts/%Y/%m/%d'),
        ),
    ]
