from django.core.validators import MinValueValidator
from django.db import models

from ExamPrepOne.account.models import Profile


# Create your models here.
class Album(models.Model):
    MUSIC_CHOICES = [
        ('POP', 'Pop Music'),
        ('JAZZ', 'Jazz Music'),
        ('RNB', 'R&B Music'),
        ('ROCK', 'Rock Music'),
        ('COUNTRY', 'Country Music'),
        ('DANCE', 'Dance Music'),
        ('HIPHOP', 'Hip Hop Music'),
        ('OTHER', 'Other'),
    ]

    album_name = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        null=False
    )

    artist = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )

    genre = models.CharField(
        max_length=30,
        choices=MUSIC_CHOICES,
        default='Other',
        blank=False,
        null=False
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False
    )

    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
        null=False,
        blank=False,
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
    )
