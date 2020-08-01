from django.db import models
import pytz


class HouseManager(models.Manager):
    """
    The system is designed to have only one House.
    """
    def get_system_house(self):
        return self.get(pk=1)

class House(models.Model):
    objects = HouseManager()

    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    timezone = models.CharField(max_length=32, choices=TIMEZONES, 
    default='UTC')


class Location(models.Model):
    structure = models.CharField(max_length=60)
    sub_structure = models.CharField(max_length=60)

    def __str__(self):
        return '{0}_{1}'.format(self.structure, self.sub_structure)

    class Meta:
        unique_together = ['structure', 'sub_structure']