from django.db import models

# Create your models here.

class User(models.Model):
    _id = models.CharField(max_length=40, primary_key=True)
    real_name = models.CharField(max_length=40)
    tz = models.CharField(max_length=40)
    
    class Meta:
        managed=False

class ActivityPeriod(models.Model):

    _id = models.CharField(max_length=40)
    start_time = models.CharField(max_length=30)
    end_time = models.CharField(max_length=30)

    class Meta:
        managed=False

    




