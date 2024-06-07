from django.db import models

# Create your models here.
class FruitStorage(models.Model):
    date = models.DateField()
    name = models.TextField()
    price = models.IntegerField()
