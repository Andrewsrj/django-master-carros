from django.shortcuts import render
from .models import Car

# Create your views here.

def cars_view(request):
    carros = Car.objects.all().order_by('model')
    context = {
        'cars': carros,
    }
    return render(request, 'cars.html', context)