from django.shortcuts import render, redirect

from Petstagram.pets.forms import PetForm, PetDeleteForm
from Petstagram.pets.models import Pets


def pet_add_page(request):
    form = PetForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)

    context = {'form': form}

    return render(request, 'pets/pet-add-page.html', context)


def pet_edit_page(request, username: str, pet_slug: str):
    pet = Pets.objects.get(slug=pet_slug)

    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile-details', username, pet_slug)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def pet_delete_page(request, username: str, pet_slug: str):
    pet = Pets.objects.get(slug=pet_slug)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)

    form = PetDeleteForm(initial=pet.__dict__)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pets/pet-delete-page.html', context)


def pet_details_page(request, username: str, pet_slug: str):
    pet = Pets.objects.get(slug=pet_slug)
    all_photo = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photo': all_photo
    }

    return render(request, 'pets/pet-details-page.html', context)
