from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    img = models.CharField(max_length=200)
    stock = models.IntegerField()