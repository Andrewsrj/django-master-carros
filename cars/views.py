from django.shortcuts import render
from cars.models import Car

# Create your views here.

def cars_view(request):
    search = request.GET.get('search')

    carros = Car.objects.filter(model__contains=search).order_by('-model') if search else Car.objects.all().order_by('-model')
    context = {
        'cars': carros,
    }
    return render(request, 'cars.html', context)

def new_car_view(request):
    return render(request, "new_car.html")