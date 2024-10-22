from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ExamPrep_WOS.profiles.forms import ProfileCreateForm
from ExamPrep_WOS.profiles.models import Profile


# Create your views here.
#
# class ProfileCreateView(CreateView):
#     model = Profile
#     form_class = ProfileCreateForm
#     template_name = 'profile/profile-create.html'
#     success_url = reverse_lazy('catalog')


def profile_creation(request):
    form = ProfileCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('catalog')

    context = {
        'form': form
    }

    return render(request, 'profile/profile-create.html', context)


def profile_details(request):
    return render(request, 'profile/profile-details.html')


def profile_edit(request):
    return render(request, 'profile/profile-edit.html')


def profile_delete(request):
    return render(request, 'profile/profile-delete.html')
