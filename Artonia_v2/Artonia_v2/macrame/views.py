from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from Artonia_v2.common.models import Product
from Artonia_v2.macrame.forms import CreateMacrameForm, EditMacrameForm, MacrameDeleteForm
from Artonia_v2.macrame.models import Macrame


class CreateMacrameView(CreateView):
    model = Product
    form_class = CreateMacrameForm
    template_name = 'macrame/create-macrame.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateMacrameView(UpdateView):
    model = Macrame
    form_class = EditMacrameForm
    template_name = 'macrame/edit-macrame.html'
    success_url = reverse_lazy('dashboard')
    pk_field = 'pk'


class MacrameDetailsView(DetailView):
    model = Macrame
    template_name = 'macrame/details-macrame.html'
    pk_url_kwarg = 'pk'


class MacrameDeleteView(DeleteView):
    model = Macrame
    form_class = MacrameDeleteForm
    pk_url_kwarg = 'pk'
    template_name = 'macrame/delete-macrame.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
