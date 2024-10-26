from django import forms

from tasty_recypes.recipe.models import Recipe


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author']

    ingredients = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'ingredient1, ingredient2, ...'
    }),
        help_text="Ingredients must be separated by a comma and space."
    )

    instructions = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Enter detailed instructions here...'
    }))

    image_url = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Optional image URL here...'
    }))
