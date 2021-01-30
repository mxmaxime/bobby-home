# Generated by Django 3.0.7 on 2020-10-01 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_auto_20200731_2128'),
        ('alarm', '0010_auto_20200928_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='camerarectangleroi',
            name='device',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='devices.Device'),
            preserve_default=False,
        ),
    ]