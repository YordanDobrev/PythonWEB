from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from ExamPrep_WOS.profiles.forms import ProfileCreateForm
from ExamPrep_WOS.profiles.models import Profile
from ExamPrep_WOS.utils import get_user_obj


class HomePage(ListView, BaseFormView):
    model = Profile
    form_class = ProfileCreateForm
    success_url = reverse_lazy('index')

    def get_template_names(self):
        profile = get_user_obj()  # None or QuerySet

        # if profile:
        #     return ['base.html']

        return ['index.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
