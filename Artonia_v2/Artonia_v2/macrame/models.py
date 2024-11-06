from django.db import models

from Artonia_v2.accounts.models import ArtoniaUser
from Artonia_v2.common.models import Product
from Artonia_v2.macrame.choices import KnotChoices


class Macrame(Product):
    user = models.ForeignKey(
        to=ArtoniaUser,
        on_delete=models.CASCADE,
        related_name='macrames',
        default=None,
    )


class KnotType(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField()

    difficulty_level = models.CharField(
        max_length=20,
        choices=KnotChoices.choices,
        default="Beginner"
    )

    image_url = models.URLField()

    macrame = models.ForeignKey(
        to=Macrame,
        on_delete=models.CASCADE,
        related_name="knot_type",
    )

    def __str__(self):
        return self.name
