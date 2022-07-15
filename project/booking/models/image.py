from django.db import models
from .apartment import Apartment

class Image(models.Model):

    photo = models.ImageField(upload_to ='apartment/% Y/% m/% d/')
    apartment = models.ForeignKey(Apartment, on_delete=models.RESTRICT)