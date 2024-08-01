from django.db import models
from django.shortcuts import render
import random 


# Create your models here.
class crc_ON(models.Model):
    circuit_id = models.IntegerField(null=True, default=1001)
    hour = models.SmallIntegerField(null=True, default=10)
    minute = models.SmallIntegerField(null=True, default=1)
    status1 = models.SmallIntegerField(null=True, default=1)
    status2 = models.SmallIntegerField(null=True, default=1)
    status3 = models.SmallIntegerField(null=True, default=1)
    status4 = models.SmallIntegerField(null=True, default=1)
    status5 = models.SmallIntegerField(null=True, default=1)
    status6 = models.SmallIntegerField(null=True, default=1)
     
    
    def __str__(self):
        return f"{self.circuit_id} {self.hour} {self.minute}"
