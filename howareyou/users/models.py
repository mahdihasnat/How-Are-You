from django.db import models
from django.utils import timezone

# Create your models here.

# -id : int
# -name : string
# -password : string
# -email : string
# -joined_at : datetime	
# -date_of_birth : datetime
# -gender : string
# -mobile_number : string


class Gender(models.TextChoices):
    MALE = "M", ("Male")
    FEMALE = "F", ("Female")

class Person(models.Model):
	id = models.CharField("unique id to every person",
                          max_length=200, primary_key=True)
	name = models.CharField(max_length=200, default="Unknown")
	
	password = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	# -joined_at : datetime	
	joined_at = models.DateTimeField(default=timezone.now)
	# -date_of_birth : datetime
	date_of_birth = models.DateTimeField(default=timezone.now,null=False,blank=False)
	# -gender 
	gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        null=False,
        blank=False,
        default=Gender.FEMALE,
    )
	# mobile_number
	mobile_number = models.CharField(null=True)

class Patient(Person):
	height = models.DecimalField("height in cm",null=True,blank=True)
	weight = models.DecimalField("weight in kg",null=True,blank=True)
	location = models.CharField("location",max_length=200,null=True,blank=True)
	info = models.CharField("info",max_length=200,null=True,blank=True)

	