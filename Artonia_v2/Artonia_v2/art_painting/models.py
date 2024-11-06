from django.db import models

from Artonia_v2.accounts.models import ArtoniaUser
from Artonia_v2.art_painting.choices import TechniqueChoice
from Artonia_v2.common.models import Product


class ArtPainting(Product):
    user = models.ForeignKey(
        to=ArtoniaUser,
        on_delete=models.CASCADE,
        related_name='art_painting',
        default=None,
    )


class Technique(models.Model):
    name = models.CharField(
        max_length=100
    )

    description = models.TextField()

    difficulty_level = models.CharField(
        max_length=20,
        choices=TechniqueChoice.choices,
        default="Other"
    )
    image_url = models.URLField()

    art_painting = models.ForeignKey(
        ArtPainting,
        on_delete=models.CASCADE,
        related_name='art_painting',
    )

    def __str__(self):
        return self.name
