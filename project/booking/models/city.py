from django.db import models
from .country import Country


class City(models.Model):

    city_name = models.CharField(max_length=50, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city_name}, {self.country.name}"