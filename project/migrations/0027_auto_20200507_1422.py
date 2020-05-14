# Generated by Django 3.0.3 on 2020-05-07 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0026_award'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Organization'),
        ),
        migrations.AddField(
            model_name='promotion',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Organization'),
        ),
        migrations.AlterField(
            model_name='award',
            name='award_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
