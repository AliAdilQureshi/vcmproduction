# Generated by Django 3.0.3 on 2020-05-04 16:42

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='organization',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='notes',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
        ),
    ]
