from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from ExamPrepOne.album.forms import CreateAlbumForm, EditAlbumForm
from ExamPrepOne.album.models import Album


# Create your views here.

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


def album_details(request, pk: int):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album,
    }

    return render(request, 'album-details.html', context)


# class EditAlbum(View):
#     model = Album
#     template_name = 'album-edit.html'
#     context_object_name = 'album'
#     success_url = reverse_lazy('index')


def album_edit(request, pk: int):
    album = Album.objects.get(pk=pk)
    form = EditAlbumForm(request.POST or None, instance=album)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('album_details', pk)

    context = {
        "form": form,
        "album": album,
    }

    return render(request, 'album-edit.html', context)


class DeleteAlbum(View):
    model = Album
    template_name = 'album-delete.html'
    context_object_name = 'album'
    success_url = reverse_lazy('index')
# def album_delete(request):
#     return render(request, 'album-delete.html', context=None)
