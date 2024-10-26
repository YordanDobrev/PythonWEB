from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from tasty_recypes.profiles.forms import ProfileCreationForm
from tasty_recypes.profiles.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('catalogue')


def profile_edit(request):
    return render(request, 'profile/edit-profile.html')


def profile_delete(request):
    return render(request, 'profile/delete-profile.html')


def profile_details(request):
    return render(request, 'profile/details-profile.html')
