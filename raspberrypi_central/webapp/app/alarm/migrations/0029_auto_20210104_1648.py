# Generated by Django 3.0.7 on 2021-01-04 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0028_auto_20201221_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cameramotiondetectedboundingbox',
            name='camera_motion_detected',
        ),
        migrations.AlterUniqueTogether(
            name='cameramotiondetectedpicture',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='cameramotiondetectedpicture',
            name='device',
        ),
        migrations.RemoveField(
            model_name='camerarectangleroi',
            name='camera_roi',
        ),
        migrations.RemoveField(
            model_name='cameraroi',
            name='device',
        ),
        migrations.DeleteModel(
            name='CameraMotionDetected',
        ),
        migrations.DeleteModel(
            name='CameraMotionDetectedBoundingBox',
        ),
        migrations.DeleteModel(
            name='CameraMotionDetectedPicture',
        ),
        migrations.DeleteModel(
            name='CameraRectangleROI',
        ),
        migrations.DeleteModel(
            name='CameraROI',
        ),
    ]
