from django.shortcuts import render

from Petstagram.pets.models import Pets


def pet_add_page(request):
    return render(request, 'pets/pet-add-page.html')


def pet_edit_page(request, username: str, pet_slug: str):
    return render(request, 'pets/pet-edit-page.html')


def pet_delete_page(request, username: str, pet_slug: str):
    return render(request, 'pets/pet-delete-page.html')


def pet_details_page(request, username: str, pet_slug: str):
    pet = Pets.objects.get(slug=pet_slug)
    all_photo = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photo': all_photo
    }

    return render(request, 'pets/pet-details-page.html', context)
