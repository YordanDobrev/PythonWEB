from django.shortcuts import render


# Create your views here.
def profile_create(request):
    return render(request, 'profile/create-profile.html')


def profile_edit(request):
    return render(request, 'profile/edit-profile.html')


def profile_delete(request):
    return render(request, 'profile/delete-profile.html')


def profile_details(request):
    return render(request, 'profile/details-profile.html')
