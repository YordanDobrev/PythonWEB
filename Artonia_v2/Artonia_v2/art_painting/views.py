from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from Artonia_v2.art_painting.forms import CreateArtPaintingForm, EditArtPaintingForm, ArtPaintingDeleteForm
from Artonia_v2.art_painting.models import ArtPainting
from Artonia_v2.common.models import Product


# Create your views here.
class CreateArtPaintingView(CreateView):
    model = Product
    form_class = CreateArtPaintingForm
    template_name = 'art_painting/create-art-painting.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateArtPaintingView(UpdateView):
    model = ArtPainting
    form_class = EditArtPaintingForm
    template_name = 'art_painting/edit-art-painting.html'
    success_url = reverse_lazy('dashboard')
    pk_field = 'pk'


class ArtPaintingDetailsView(DetailView):
    model = ArtPainting
    template_name = 'art_painting/details-art-painting.html'
    pk_url_kwarg = 'pk'


class ArtPaintingDeleteView(DeleteView):
    model = ArtPainting
    form_class = ArtPaintingDeleteForm
    pk_url_kwarg = 'pk'
    template_name = 'art_painting/delete-art-painting.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)