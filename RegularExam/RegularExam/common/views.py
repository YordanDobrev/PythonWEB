from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from RegularExam.author.forms import AuthorCreateForm
from RegularExam.post.models import Post
from RegularExam.utils import get_user_obj


# Create your views here.
class HomePage(ListView, BaseFormView):
    model = Post
    form_class = AuthorCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self, **kwargs):
        profile = get_user_obj()
        if not profile:
            return ['index.html']

        return ['dashboard.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# def dashboard(request):
#     profile = get_user_obj()
#     posts = Post.objects.filter(pk=profile.pk)
#
#     context = {
#         'profile': profile,
#         'posts': posts,
#     }
#
#     render(request, 'dashboard.html', context)

def dashboard(request):
    profile = get_user_obj()
    posts = Post.objects.filter(pk=profile.pk)

    context = {
        'profile': profile,
        'posts': posts,
    }

    return render(request, 'dashboard.html', context)
