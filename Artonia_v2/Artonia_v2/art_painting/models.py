from django.db import models
from Artonia_v2.accounts.models import ArtoniaUser
from Artonia_v2.art_painting.choices import TechniqueChoice
from Artonia_v2.common.models import Product


class ArtPainting(Product):
    technique_name = models.CharField(
        max_length=20,
        choices=TechniqueChoice.choices,
        default="Other"
    )

    technique_description = models.TextField(
        blank=True,
        null=True
    )

    user = models.ForeignKey(
        to=ArtoniaUser,
        on_delete=models.CASCADE
    )

    is_public = models.BooleanField(
        default=False
    )

    views_count = models.PositiveIntegerField(
        default=0
    )

    likes = models.ManyToManyField(
        to=ArtoniaUser,
        related_name='liked_paintings',
        blank=True
    )

    @property
    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return self.name
