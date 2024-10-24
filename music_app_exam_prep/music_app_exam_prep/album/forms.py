from django import forms
from music_app_exam_prep.album.models import Album
from music_app_exam_prep.mixins import PlaceholderMixin


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)


class CreateAlbumForm(PlaceholderMixin, AlbumBaseForm):
    pass
