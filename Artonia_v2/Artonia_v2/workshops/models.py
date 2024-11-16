from django.conf import settings
from django.db import models
from Artonia_v2.accounts.models import ArtoniaUser


class Workshop(models.Model):
    title = models.CharField(
        max_length=200
    )

    instructor = models.ForeignKey(
        to=ArtoniaUser,
        on_delete=models.CASCADE,
    )

    description = models.TextField()

    materials_provided = models.TextField()

    prerequisites = models.TextField()

    date = models.DateTimeField()

    duration_hours = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )

    location = models.CharField(
        max_length=200
    )

    is_online = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )

    meeting_url = models.URLField(
        blank=True,
        null=True,
    )

    capacity = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image_url = models.URLField()

    participants = models.ManyToManyField(
        to=ArtoniaUser,
        related_name='workshops_enrolled',
        through='WorkshopRegistration'
    )

    def __str__(self):
        return self.title


class WorkshopRegistration(models.Model):
    workshop = models.ForeignKey(
        to=Workshop,
        on_delete=models.CASCADE
    )

    participant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    registration_date = models.DateTimeField(
        auto_now_add=True
    )

    payment_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('refunded', 'Refunded')
    ])

    attended = models.BooleanField(default=False)

    class Meta:
        unique_together = ['workshop', 'participant']
