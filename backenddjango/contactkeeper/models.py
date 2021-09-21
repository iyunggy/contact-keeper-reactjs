from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Contact(models.Model):
  id = models.AutoField(primary_key=True)
  date = models.DateField(default=datetime.date.today)
  name = models.CharField(max_length=255, default='')
  email = models.CharField(max_length=255, default='')
  phone = models.CharField(max_length=255, default='')
  type = models.CharField(max_length=255, default='')

