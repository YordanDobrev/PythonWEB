from django import forms

from Artonia_v2.macrame.models import Macrame


class CreateMacrameForm(forms.ModelForm):
    class Meta:
        model = Macrame
        exclude = ['created_at', 'updated_at', 'user']

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Macrame name...'}))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Description...'
    }))

    price = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Price...'
    }))

    image_url = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Put Macrame URL...'
    }))

    knot_type = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Put a knot type...'}))

    knot_description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Short Knot Description...'
    }))
