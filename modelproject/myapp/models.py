from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    dob = models.DateField()
    place = models.CharField(max_length=80)
    brach = models.CharField(max_length=80)
    mobile = models.CharField(max_length=11)
    marks = models.IntegerField()
    def __str__(self):
        return self.name
   
    