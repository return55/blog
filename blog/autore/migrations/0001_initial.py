# Generated by Django 2.1.2 on 2018-11-19 17:44

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(blank=True, default='', max_length=20)),
                ('last_name', models.CharField(blank=True, default='', max_length=20)),
                ('data_registrazione', models.DateField(default=datetime.date.today, editable=False)),
                ('bio', models.TextField(blank=True)),
                ('profilo_pubblico', models.BooleanField(blank=True, default=False)),
                ('articoli_votati', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0, editable=False), default=list, editable=False, size=None)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('is_admin', models.BooleanField(blank=True, default=False)),
            ],
            options={
                'verbose_name_plural': 'Autori',
                'get_latest_by': ['first_name', 'last_name'],
            },
        ),
    ]
