from django.db.models.functions import datetime
from django.utils import timezone

from Artonia_v2.mixins import ReadOnlyMixin
from Artonia_v2.workshops.models import Workshop
from django import forms


class CreateWorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = '__all__'

    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Workshop name...'}))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Workshop description...'
    }))

    materials_provided = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Materials provided...'
    }))

    prerequisites = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Prerequisites...'
    }))

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=timezone.now().date
    )

    duration_hours = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'type': 'number',
        })
    )

    location = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Location...'
    }))

    is_online = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        }),
        required=False
    )

    meeting_url = forms.CharField(widget=forms.URLInput(attrs={
        'placeholder': 'Meeting URL...'
    }),
        required=False
    )

    capacity = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Capacity...'
        })
    )

    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Price...'
        })
    )

    image_url = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Put Macrame URL...'
    }))


class UpdateWorkshopForm(CreateWorkshopForm):
    pass


class DeleteWorkshopForm(ReadOnlyMixin, forms.ModelForm):
    class Meta:
        model = Workshop
        exclude = ['instructor', 'participants', 'is_online']

    read_only_fields = ['title', 'description', 'materials_provided', 'prerequisites', 'date', 'duration_hours',
                        'location', 'meeting_url', 'capacity', 'price', 'image_url'
                        ]
