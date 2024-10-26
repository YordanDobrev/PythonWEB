from django.shortcuts import render


# Create your views here.

def recipe_catalog(request):
    return render(request, 'recipe/catalogue.html')


def recipe_creation(request):
    return render(request, 'recipe/create-recipe.html')


def recipe_details(request):
    return render(request, 'recipe/details-recipe.html')


def recipe_edit(request):
    return render(request, 'recipe/edit-recipe.html')

def recipe_delete(request):
    return render(request, 'recipe/delete-recipe.html')