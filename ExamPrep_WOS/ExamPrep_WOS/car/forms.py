from django import forms

from ExamPrep_WOS.car.models import Car


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']

    image_url = forms.URLField(
        widget=forms.TextInput(attrs={
            'placeholder': 'https://...'
        }))


class CarDetailForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']
