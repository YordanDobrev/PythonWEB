from django import template

from tasty_recypes.utils import get_user_obj

register = template.Library()


@register.filter
def ingredients_split(value, delimiter=', '):
    recipe_ingredients = value.recipe_ingredients.all()
    return recipe_ingredients.split(delimiter)
