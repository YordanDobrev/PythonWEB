from django.db import models


class Product(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(
        max_length=100
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


class Macrame(Product):

    def __str__(self):
        return self.name


class ArtPainting(Product):

    def __str__(self):
        return self.name
