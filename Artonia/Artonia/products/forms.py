from django import forms
from Artonia.products.models import Macrame


class ProductForm(forms.ModelForm):
    class Meta:
        model = Macrame
        fields = '__all__'
