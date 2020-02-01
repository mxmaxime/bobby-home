# Generated by Django 3.0.2 on 2020-01-22 18:03

import devices.models
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devices', '0006_device_device_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='severity',
            field=models.IntegerField(choices=[(devices.models.SeverityChoice['LOW'], 'low'), (devices.models.SeverityChoice['MODERATE'], 'moderate'), (devices.models.SeverityChoice['HIGH'], 'high')]),
        ),
        migrations.CreateModel(
            name='UserCommunication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AlertNotificationSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severity', models.IntegerField(choices=[(devices.models.SeverityChoice['LOW'], 'low'), (devices.models.SeverityChoice['MODERATE'], 'moderate'), (devices.models.SeverityChoice['HIGH'], 'high')])),
                ('alert_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='devices.AlertType')),
                ('communication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.UserCommunication')),
            ],
        ),
    ]
