from django.shortcuts import render


# Create your views here.

def car_catalog(request):
    return render(request, 'catalogue.html')


def create_car(request):
    return render(request, 'car/car-create.html')


def car_details(request):
    return render(request, 'car/car-details.html')


def car_edit(request):
    return render(request, 'car/car-edit.html')


def car_delete(request):
    return render(request, 'car/car-delete.html')
