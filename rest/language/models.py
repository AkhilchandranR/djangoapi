from django.db import models

class paradigm(models.Model):
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Languages(models.Model):
	name=models.CharField(max_length=100)
	paradigm=models.ForeignKey(paradigm,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name

class programmer(models.Model):
	name=models.CharField(max_length=100)
	language=models.ManyToManyField(Languages)
	
	def __str__(self):
		return self.name