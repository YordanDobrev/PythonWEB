from django.shortcuts import render
from django.views import View

from ExamPrepOne.account.forms import ProfileCreationForm
from ExamPrepOne.account.models import Profile


# Create your views here.


def home_view(request):
    form = ProfileCreationForm(request.POST or None)

    if form.is_valid():
        # If the form is valid, save the data to create a new Profile object
        profile = form.save(commit=False)  # Use commit=False if you want to add extra data before saving
        profile.save()

        # Retrieve the data from the form
        username = profile.username
        email = profile.email
        age = profile.age

        context = {
            'form': form,
            'username': username,
            'email': email,
            'age': age
        }
    else:
        context = {
            'form': form,
            'errors': form.errors,  # Pass the errors to the context
        }

    return render(request, 'home-no-profile.html', context)


class ProfileDetailsView(View):
    model = Profile
    context_object_name = 'profile'
    success_url = 'profile-details.html'
    form_class = ProfileCreationForm


# def profile_details(request):
#     return render(request, 'profile-details.html', context=None)


class DeleteProfileView(View):
    model = Profile
    context_object_name = 'profile'
    success_url = 'profile-delete.html'

# def profile_delete(request):
#     return render(request, 'profile-delete.html', context=None)
