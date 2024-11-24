from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from Artonia_v2.accounts.models import ArtoniaUser


class ArtworkCategory(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField()

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Artwork Categories"


class Artwork(models.Model):
    ARTWORK_TYPES = [
        ('macrame', 'Macrame'),
        ('painting', 'Painting'),
    ]

    VISIBILITY_CHOICES = [
        ('private', 'Private'),
        ('public', 'Public'),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField()

    artwork_type = models.CharField(max_length=20, choices=ARTWORK_TYPES)

    category = models.ForeignKey(ArtworkCategory, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    creator = models.ForeignKey(ArtoniaUser, on_delete=models.CASCADE)

    is_featured = models.BooleanField(default=False)

    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='private')

    slug = models.SlugField(unique=True)

    likes = models.ManyToManyField(ArtoniaUser, related_name='liked_artworks', blank=True)

    views_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title} by {self.creator.username}"


class ArtworkComment(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='comments')

    author = models.ForeignKey(ArtoniaUser, on_delete=models.CASCADE)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


class ArtworkShare(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='shares')

    shared_by = models.ForeignKey(ArtoniaUser, on_delete=models.CASCADE)

    shared_at = models.DateTimeField(auto_now_add=True)

    share_message = models.TextField(blank=True)

    class Meta:
        ordering = ['-shared_at']
