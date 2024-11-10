from django.urls import reverse_lazy
from django.views.generic import CreateView

from Artonia_v2.art_painting.forms import CreateArtPaintingForm
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
