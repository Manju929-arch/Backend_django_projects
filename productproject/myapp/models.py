from django.db import models

# Create your models here.
class product(models.Model):
    p_name = models.CharField(max_length=100)
    p_manfacture = models.IntegerField()
    p_exp = models.IntegerField()
    p_mail = models.EmailField()
    def __str__(self):
        return self.p_name