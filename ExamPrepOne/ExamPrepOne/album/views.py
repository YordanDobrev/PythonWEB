from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from ExamPrepOne.album.forms import CreateAlbumForm
from ExamPrepOne.album.models import Album


# Create your views here.


# class AddAlbum(View):
#     model = Album
#     template_name = 'album-add.html'
#     context_object_name = 'album'

def add_album(request):
    album_form = CreateAlbumForm(request.POST or None, request.FILES)

    if request.method == 'POST':
        if album_form.is_valid():
            album_form.save()
            return redirect('index')

    context = {
        'album_form': album_form,
    }

    return render(request, 'album-add.html', context)


class DetailsAlbum(View):
    model = Album
    template_name = 'album-details.html'
    context_object_name = 'album'

# def album_details(request):
#     return render(request, 'album-details.html', context=None)


class EditAlbum(View):
    model = Album
    template_name = 'album-edit.html'
    context_object_name = 'album'
    success_url = reverse_lazy('index')
# def album_edit(request):
#     return render(request, 'album-edit.html', context=None)


class DeleteAlbum(View):
    model = Album
    template_name = 'album-delete.html'
    context_object_name = 'album'
    success_url = reverse_lazy('index')
# def album_delete(request):
#     return render(request, 'album-delete.html', context=None)
