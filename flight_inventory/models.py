from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile_number = models.CharField(max_length=15)
    email = models.CharField(max_length=100, unique=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    
class Airport(models.Model):
    iata_code = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)

class Flight(models.Model):
    # origin = models.CharField(max_length=100)
    # destination = models.CharField(max_length=100)
    origin = models.ForeignKey(Airport, related_name='departure_airport', on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport, related_name='arrival_airport', on_delete=models.CASCADE)
    flight_number = models.IntegerField()
    departure_date_time = models.DateTimeField()
    arrival_date_time = models.DateTimeField()
    base_fare = models.CharField(max_length=100)
    tax = models.CharField(max_length=100)



    




