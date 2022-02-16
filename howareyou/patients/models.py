from django.db import models

from persons.models import Person
# Create your models here.


class Patient(Person):
	height = models.DecimalField("height in cm",null=True,blank=True,decimal_places=2,max_digits=10)
	weight = models.DecimalField("weight in kg",null=True,blank=True,decimal_places=2,max_digits=10)
	location = models.CharField("location",max_length=200,null=True,blank=True)
	info = models.CharField("info",max_length=200,null=True,blank=True)
