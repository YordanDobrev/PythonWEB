from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from RegularExam.author.forms import AuthorCreateForm
from RegularExam.author.models import Author


class AuthorCreationView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'author/create-author.html'
    success_url = reverse_lazy('home')


def author_details(request):
    return render(request, 'author/details-author.html')


def author_edit(request):
    return render(request, 'author/edit-author.html')


def author_delete(request):
    return render(request, 'author/delete-author.html')
