from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm

# Create your views here.

def cars_view(request):
    search = request.GET.get('search')

    carros = Car.objects.filter(model__contains=search).order_by('-model') if search else Car.objects.all().order_by('-model')
    context = {
        'cars': carros,
    }
    return render(request, 'cars.html', context)

def new_car_view(request):
    if request.method == "POST":
        new_car_form = CarForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarForm()
    
    context = {
        'new_car_form': new_car_form
    }
    return render(request, "new_car.html", context)