from django.db import models

from django.conf import settings

# Create your models here.

class Airport(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.code})"
class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    departure_airport = models.ForeignKey(Airport, related_name='departures', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    created_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="created_flights"
)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.flight_number}: {self.departure_airport.code} -> {self.arrival_airport.code}"
    