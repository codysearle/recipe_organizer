# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_organizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='', help_text=b'This is a quick description of your recipe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='directions',
            field=models.TextField(default=' ', help_text=b'How to make the recipe'),
            preserve_default=False,
        ),
    ]
