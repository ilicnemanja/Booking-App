from django.shortcuts import render
from django.http import HttpResponse
# from .models.person import Person
from datetime import date

def current_year():
    current_year = date.today().year
    return current_year


def index(request):
    year = current_year()
    return render(request, 'index.html', context= {'year': year})