from django.db import models
from .person import Person
from .address import Address


class Apartment(models.Model):

    STARS = (
        (0, 'Zero'),
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    )

    name = models.CharField(max_length=150, null=False)
    rate = models.IntegerField(default=0, choices=STARS, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    description = models.TextField(null=True, blank=True)
    available = models.BooleanField(default=True)
    rooms = models.IntegerField(default=1)
    parking = models.BooleanField(default=True)
    free_wifi = models.BooleanField(default=True)
    pets_friendly = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=True)
    bathroom = models.BooleanField(default=True)
    terrace = models.BooleanField(default=False)
    city_view = models.BooleanField(default=False)
    smoker = models.BooleanField(default=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    owner = models.ForeignKey(Person, on_delete=models.DO_NOTHING)


    def __str__(self):
       return f"{self.name}  {int(self.price)}e/ per night"
   