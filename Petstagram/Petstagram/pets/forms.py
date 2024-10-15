from django import forms

from Petstagram.pets.models import Pets


class PetForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields = ['name', 'date_of_birth', 'personal_photo']
