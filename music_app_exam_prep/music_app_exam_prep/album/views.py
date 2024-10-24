from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from music_app_exam_prep.album.forms import CreateAlbumForm
from music_app_exam_prep.album.models import Album
from music_app_exam_prep.utils import get_user_obj


# Create your views here.

class AlbumCreateView(CreateView):
    model = Album
    form_class = CreateAlbumForm
    template_name = 'album/album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


def album_details(request):
    return render(request, 'album/album-details.html')


def album_edit(request):
    return render(request, 'album/album-edit.html')


def album_delete(request):
    return render(request, 'album/album-delete.html')
