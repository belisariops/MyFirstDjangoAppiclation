# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebAplication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.IntegerField()),
                ('hospital_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_rut', models.CharField(max_length=50)),
                ('patient_name', models.CharField(max_length=50)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebAplication.Hospital')),
            ],
        ),
    ]
