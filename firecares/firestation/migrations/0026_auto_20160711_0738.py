# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import firecares.firestation.models


class Migration(migrations.Migration):

    dependencies = [
        ('firestation', '0025_auto_20160627_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(storage=firecares.firestation.models.DocumentS3Storage(bucket=b'firecares-uploads-test'), upload_to=firecares.firestation.models.document_upload_to),
        ),
    ]
