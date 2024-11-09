from django.db import models

from Artonia_v2.accounts.models import ArtoniaUser
from Artonia_v2.common.models import Product
from Artonia_v2.macrame.choices import KnotChoices


class Macrame(Product):
    user = models.ForeignKey(
        to=ArtoniaUser,
        on_delete=models.CASCADE,
    )

    knot_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    knot_description = models.TextField(
        blank=True,
        null=True,
    )

    difficulty_level = models.CharField(
        max_length=20,
        choices=KnotChoices.choices,
        default="Beginner"
    )

    def __str__(self):
        return self.name
