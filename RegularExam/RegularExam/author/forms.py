from django import forms

from RegularExam.author.models import Author


class AuthorCreateForm(forms.ModelForm):
    passcode = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Author
        fields = '__all__'
