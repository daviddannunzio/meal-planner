# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-25 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_auto_20160402_1801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipestep',
            options={'ordering': ['step_number']},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='meat',
            field=models.CharField(choices=[(b'V', b'Veggie'), (b'T', b'Tofu'), (b'C', b'Chicken'), (b'F', b'Fish'), (b'B', b'Beef'), (b'P', b'Pork'), (b'VEGAN', b'Vegan')], max_length=1),
        ),
    ]
