from django.db import models
from Artonia_v2.accounts.models import ArtoniaUser
from Artonia_v2.art_painting.choices import TechniqueChoice

from django.contrib.contenttypes.fields import GenericRelation

from Artonia_v2.common.models import Product, Like


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

    likes = GenericRelation(Like)

    def total_likes(self):
        return self.likes.count()
