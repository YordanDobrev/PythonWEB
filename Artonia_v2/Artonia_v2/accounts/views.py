from django.urls import reverse_lazy
from django.views.generic import CreateView

from Artonia_v2.accounts.forms import CustomUserCreationForm


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')
