from django.urls import reverse_lazy
from django.views.generic import CreateView

from Artonia_v2.common.models import Product
from Artonia_v2.macrame.forms import CreateMacrameForm


class CreateMacrameView(CreateView):
    model = Product
    form_class = CreateMacrameForm
    template_name = 'macrame/create-macrame.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)