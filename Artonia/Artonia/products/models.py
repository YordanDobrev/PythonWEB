from django.db import models
from Artonia.products.validators import bad_words


class Product(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    description = models.TextField(
        validators=[bad_words]
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now=True)


class Macrame(Product):

    def __str__(self):
        return self.name


class ArtPainting(Product):

    def __str__(self):
        return self.name
