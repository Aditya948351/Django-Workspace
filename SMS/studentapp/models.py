from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll = models.IntegerField()
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField(max_length=100)