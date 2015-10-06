# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherfeedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='city',
            field=models.CharField(help_text="School's city", max_length=255),
        ),
        migrations.AlterField(
            model_name='school',
            name='country',
            field=models.CharField(help_text="School's country", max_length=255),
        ),
        migrations.AlterField(
            model_name='school',
            name='province',
            field=models.CharField(help_text="School's province", max_length=255),
        ),
    ]
