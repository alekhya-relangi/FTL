from django.db import models
import factory  
import factory.django
from django.utils import timezone
from django.db.models import DateTimeField

# Create your models here.

class members(models.Model):
    
    m_id = models.CharField(max_length=80)
    real_name = models.CharField(max_length=70)
    tz= models.CharField(max_length=60)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField() 
    
    def __str__(self):
        return self.m_id
    
