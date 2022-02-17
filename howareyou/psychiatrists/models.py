
from django.db import models

from persons.models import Person

# Create your models here.
class Award(models.Model):
	name = models.CharField(max_length=100)
	host = models.CharField(max_length=100)

class PsychiatristAward(models.Model):
	psychiatrist = models.ForeignKey('psychiatrists.Psychiatrist', on_delete=models.CASCADE)
	award = models.ForeignKey(Award, on_delete=models.CASCADE)
	description = models.TextField()
	date = models.DateField()


class Degree(models.Model):
	name = models.CharField(max_length=100)

class PsychiatristDegree(models.Model):
	psychiatrist = models.ForeignKey('psychiatrists.Psychiatrist', on_delete=models.CASCADE)
	degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
	description = models.TextField()
	institutuion = models.CharField(max_length=100)
	graduation_date = models.DateField()

class Expertise(models.Model):
	field_name = models.CharField(max_length=100)

class PsychiatristExpertise(models.Model):
	psychiatrist = models.ForeignKey('psychiatrists.Psychiatrist', on_delete=models.CASCADE)
	expertise = models.ForeignKey(Expertise, on_delete=models.CASCADE)
	decription = models.TextField()

class Psychiatrist(Person):
	verified = models.BooleanField(default=False)
	available_times = models.TextField(max_length=100,null=True,blank=True)
	awards = models.ManyToManyField(Award , through=PsychiatristAward)
	degrees = models.ManyToManyField(Degree , through=PsychiatristDegree)
	expertises = models.ManyToManyField(Expertise , through=PsychiatristExpertise)

class ReviewBoardMember(Psychiatrist):
	pass

