from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
 #customer array see if new groups can be created in magento and add module
 email = models.CharField(max_length=150, unique=True,blank=True)
 name  = models.CharField(max_length=150,blank=True )
 address = models.ForeignKey('CustomerAddress')
 phone_number = models.CharField(max_length=12 ,blank=True)
 
class CustomerAddress(models.Model):
   
    line_1 = models.CharField(max_length=300 ,blank=True)
    line_2 = models.CharField(max_length=300 ,blank=True)
    line_3 = models.CharField(max_length=300 ,blank=True)
    city = models.CharField(max_length=150 ,blank=True)
    postalcode = models.CharField(max_length=10 ,blank=True)
    state = models.CharField(max_length=150,blank=True )
    country = models.CharField(max_length=150 ,blank=True) 


