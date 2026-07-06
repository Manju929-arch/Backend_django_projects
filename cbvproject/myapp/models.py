from django.db import models
from django.urls import reverse

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=80)
    email = models.EmailField()
    

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse ('detail',kwargs = {'pk':self.pk})
    

