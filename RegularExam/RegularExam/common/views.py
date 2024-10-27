from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from RegularExam.author.forms import AuthorCreateForm
from RegularExam.post.models import Post


# Create your views here.
class HomePage(ListView, BaseFormView):
    model = Post
    form_class = AuthorCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        return ['index.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)