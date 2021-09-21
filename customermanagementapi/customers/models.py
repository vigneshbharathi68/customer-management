from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    occupation = models.CharField(max_length=200)
    dob = models.DateField()
    address = models.CharField(max_length=500)
