from django.urls import reverse_lazy

from Artonia_v2.workshops.forms import CreateWorkshopForm, DeleteWorkshopForm
from Artonia_v2.workshops.models import Workshop
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class WorkshopListView(ListView):
    model = Workshop
    template_name = 'workshops/workshop_list.html'
    context_object_name = 'workshops'
    paginate_by = 10


class WorkshopDetailView(DetailView):
    model = Workshop
    template_name = 'workshops/workshop_detail.html'


class WorkshopCreateView(LoginRequiredMixin, CreateView):
    model = Workshop
    form_class = CreateWorkshopForm
    template_name = 'workshops/workshop_form.html'
    success_url = reverse_lazy('workshop-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WorkshopDeleteView(DeleteView):
    model = Workshop
    form_class = DeleteWorkshopForm
    pk_url_kwarg = 'pk'
    template_name = 'workshops/workshop-delete.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
