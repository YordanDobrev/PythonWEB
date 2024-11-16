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
        input_formats=['%Y-%m-%d', '%d-%m-%Y'],
        widget=forms.DateInput(attrs={'type': 'date'})
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
        })
    )

    meeting_url = forms.CharField(widget=forms.URLInput(attrs={
        'placeholder': 'Meeting URL...'
    }))

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


class DeleteWorkshopForm(ReadOnlyMixin, forms.ModelForm):
    class Meta:
        model = Workshop
        exclude = ['instructor', 'participants']

    read_only_fields = ['title', 'description', 'materials_provided', 'prerequisites', 'date', 'duration_hours',
                        'location', 'is_online', 'meeting_url', 'capacity', 'price', 'image_url'
                        ]
