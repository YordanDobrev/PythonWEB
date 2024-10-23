from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ExamPrep_WOS.car.forms import CarCreateForm
from ExamPrep_WOS.car.models import Car
from ExamPrep_WOS.utils import get_user_obj


# Create your views here.

def car_catalog(request):
    profile = get_user_obj()
    cars = profile.car_set.all()

    context = {
        'profile': profile,
        'cars': cars,
    }

    return render(request, 'car/catalogue.html', context)


class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'car/car-create.html'
    success_url = reverse_lazy('catalog')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


def car_details(request):
    return render(request, 'car/car-details.html')


def car_edit(request):
    return render(request, 'car/car-edit.html')


def car_delete(request):
    return render(request, 'car/car-delete.html')
