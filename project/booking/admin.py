from django.contrib import admin
from .models import *


admin.site.register(person.Person)
admin.site.register(address.Address)
admin.site.register(city.City)
admin.site.register(country.Country)
admin.site.register(Apartment)
admin.site.register(image.Image)
admin.site.register(reservation.Reservation)