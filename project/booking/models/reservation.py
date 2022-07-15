from django.db import models
from .apartment import Apartment
from .person import Person
import pandas as pd

class Reservation(models.Model):

    date_started = models.DateField(null=False, unique=True)
    date_end = models.DateField(null=False, unique=True)
    total_price = models.FloatField()
    adults = models.IntegerField(default=1)
    children = models.IntegerField(default=0)
    customer = models.ForeignKey(Person,  on_delete=models.CASCADE, null=False)
    apartment = models.ForeignKey(Apartment,  on_delete=models.CASCADE, null=False)


    def __str__(self) -> str:
        days = len(pd.date_range(start=self.date_started,end=self.date_end). to_pydatetime())-1
        return f"The price per night is {int(self.apartment.price)}e, {self.customer.first_name} booked for {days} nights and the total price is {self.get_total_price()}e"


    def get_total_price(self):
        days = len(pd.date_range(start=self.date_started,end=self.date_end). to_pydatetime())-1
        total_price = int(self.apartment.price * days)
        return total_price