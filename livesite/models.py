from django.db import models
# Create your models here.

class comapny(models.Model):
    name=models.CharField(max_length=10)
    contact=models.IntegerField()
    country=models.CharField(max_length=10)
    