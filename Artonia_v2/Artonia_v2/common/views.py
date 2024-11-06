from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from Artonia_v2.art_painting.models import ArtPainting
from Artonia_v2.forms import CustomUserForm
from Artonia_v2.macrame.models import Macrame
from Artonia_v2.utils import get_user_obj


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
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def dashboard(request):
    profile = get_user_obj()
    macrame = Macrame.objects.filter(user=profile)
    art_paint = ArtPainting.objects.filter(user=profile)

    context = {
        'profile': profile,
        'macrame': macrame,
        'art_paint': art_paint,
    }

    return render(request, 'dashboard.html', context)
