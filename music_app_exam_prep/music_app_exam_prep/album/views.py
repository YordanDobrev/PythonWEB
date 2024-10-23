from django.shortcuts import render


# Create your views here.
def add_album(request):
    return render(request, 'album/album-add.html')


def album_details(request):
    return render(request, 'album/album-details.html')


def album_edit(request):
    return render(request, 'album/album-edit.html')


def album_delete(request):
    return render(request, 'album/album-delete.html')
