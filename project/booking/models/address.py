from django.db import models
from .city import City


class Address(models.Model):

    street = models.CharField(max_length=100, null=False)
    postcode = models.IntegerField(null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.street} ({self.city.city_name}, {self.city.country.name})"
    