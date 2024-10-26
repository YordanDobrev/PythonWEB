from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from tasty_recypes.recipe.forms import RecipeCreateForm
from tasty_recypes.recipe.models import Recipe
from tasty_recypes.utils import get_user_obj


# Create your views here.

def recipe_catalog(request):
    return render(request, 'recipe/catalogue.html')


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipe/create-recipe.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe/details-recipe.html'
    pk_url_kwarg = 'id'


# def recipe_details(request):
#     return render(request, 'recipe/details-recipe.html')


def recipe_edit(request):
    return render(request, 'recipe/edit-recipe.html')


def recipe_delete(request):
    return render(request, 'recipe/delete-recipe.html')
