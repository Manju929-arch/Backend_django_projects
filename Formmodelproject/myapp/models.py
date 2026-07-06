from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    place = models.CharField(max_length=80)
    def __str__(self):
        return self.name
