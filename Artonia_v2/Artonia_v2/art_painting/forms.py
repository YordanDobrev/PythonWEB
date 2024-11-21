from django import forms

from Artonia_v2.art_painting.models import ArtPainting
from Artonia_v2.mixins import ReadOnlyMixin


class CreateArtPaintingForm(forms.ModelForm):
    class Meta:
        model = ArtPainting
        exclude = ['created_at', 'updated_at', 'user']

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Art Painting name...'}))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Description...'
    }))

    price = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Price...'
    }))

    image_url = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Put Art painting URL...'
    }))

    technique_description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Short technique description...'
    }))


class EditArtPaintingForm(CreateArtPaintingForm):
    pass


class ArtPaintingDeleteForm(ReadOnlyMixin, forms.ModelForm):
    class Meta:
        model = ArtPainting
        exclude = ['created_at', 'updated_at', 'user']

    image_url = forms.CharField(
        label='Post Image URL:'
    )

    read_only_fields = ['name', 'description', 'price', 'image_url', 'technique_name', 'technique_description']