from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from Artonia_v2.art_painting.models import ArtPainting
from Artonia_v2.forms import CustomUserForm
from Artonia_v2.macrame.models import Macrame
from Artonia_v2.utils import get_user_obj
from Artonia_v2.workshops.models import Workshop


# Create your views here.
class HomePage(FormView):
    template_name = 'index.html'
    form_class = CustomUserForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_user_obj()
        context['macrame_list'] = Macrame.objects.all()
        context['art_painting_list'] = ArtPainting.objects.all()
        context['profile'] = profile
        context['workshop_list'] = Workshop.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registered_workshops'] = Workshop.objects.filter(participants=self.request.user)
        context['macrames'] = Macrame.objects.filter(user=self.request.user)
        context['art_paint'] = ArtPainting.objects.filter(user=self.request.user)
        context['is_instructor'] = self.request.user.groups.filter(name='Instructor').exists()
        return context


@login_required
def toggle_artwork_visibility(request, pk, artwork_type):
    if artwork_type == 'macrame':
        artwork = get_object_or_404(Macrame, pk=pk)
    else:
        artwork = get_object_or_404(ArtPainting, pk=pk)

    if request.method == 'POST':
        artwork.is_public = not artwork.is_public
        artwork.save()

        status = "public" if artwork.is_public else "private"
        messages.success(request, f'Your {artwork_type} is now {status}.')

    return redirect('dashboard')
