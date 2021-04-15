from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone=models.CharField(max_length=12,blank=False)

class Sell(models.Model):
    name=models.CharField(max_length=15)
    desc=models.CharField(max_length=299)
    price=models.CharField(max_length=5)
    image=models.ImageField(null=True,blank=True)
    phone=models.CharField(max_length=10)
    # pub_date = models.DateField()
    
    # class Meta:
