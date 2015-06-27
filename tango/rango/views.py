from django.http import request
from django.shortcuts import render


# Create your views here.
def rango(request):
    return render(request, 'rango/rango.html')
