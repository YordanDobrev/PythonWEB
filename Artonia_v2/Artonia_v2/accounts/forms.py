from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'image_url', 'description')

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name...'},
    ))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name...',
    }))

    image_url = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Place Image URL...',
    }),
        required=False,
    )

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Short description of yourself...',
    }))
