# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-02 17:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('unit', models.CharField(max_length=100)),
                ('preparation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('website', models.URLField()),
                ('meat', models.CharField(choices=[(b'V', b'Veggie'), (b'T', b'Tofu'), (b'C', b'Chicken'), (b'F', b'Fish'), (b'B', b'Beef'), (b'P', b'Pork')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_number', models.IntegerField()),
                ('step_description', models.CharField(max_length=400)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='ingredients',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.Recipe'),
        ),
    ]
