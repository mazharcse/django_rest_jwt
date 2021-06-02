from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    code = models.CharField(max_length=10)

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Address(models.Model):
    name = models.CharField(max_length=100)
    house_number = models.CharField(max_length=50)
    road_number = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)