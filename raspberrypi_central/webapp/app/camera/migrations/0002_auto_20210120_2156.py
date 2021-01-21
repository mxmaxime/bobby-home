# Generated by Django 3.0.7 on 2021-01-20 21:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cameramotiondetected',
            name='motion_ended_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cameramotiondetected',
            name='motion_started_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 20, 21, 54, 58, 609522, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cameramotiondetected',
            name='event_ref',
            field=models.UUIDField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='cameramotiondetected',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='cameramotiondetected',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='cameramotiondetected',
            name='is_motion',
        ),
    ]
