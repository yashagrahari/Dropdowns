from django.db import models

# Create your models here.

class course(models.Model):
	co=models.CharField(max_length=100)


class branch(models.Model):
	link1=models.ForeignKey(course, on_delete=models.CASCADE)
	br=models.CharField(max_length=100)

class sem(models.Model):
	link2=models.ForeignKey(branch, on_delete=models.CASCADE)
	sems=models.CharField(max_length=100)

class section(models.Model):
	link3=models.ForeignKey(sem, on_delete=models.CASCADE)
	sec=models.CharField(max_length=100)
		

		
