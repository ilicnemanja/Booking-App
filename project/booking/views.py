from django.shortcuts import render
from django.http import HttpResponse
# from .models.person import Person

def index(request):
    
    return render(request, 'index.html')