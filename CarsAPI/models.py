from django.db import models

# Create your models here.

class Cars(models.Model):
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=20)
    price = models.IntegerField()
