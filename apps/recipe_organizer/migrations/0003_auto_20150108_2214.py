# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_organizer', '0002_auto_20150108_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(help_text=b'This is a quick description of your recipe', null=True, blank=True),
            preserve_default=True,
        ),
    ]
