from django.http import HttpResponse
from django.shortcuts import render, redirect

from Artonia.products.forms import ProductForm
from Artonia.products.models import ArtPainting, Macrame


# Create your views here.

def index(request):
    art_paintings = request.GET.get('art_paintings', '')
    art_paintings = ArtPainting.objects.filter(name__icontains=art_paintings)

    macrame = request.GET.get('macrame', '')
    macrame = Macrame.objects.filter(name__icontains=macrame)

    context = {
        'art_paintings': art_paintings,
        'macrame': macrame,
    }

    return render(request, 'products_in_table.html', context)


def add_macrame(request):
    macrame_form = ProductForm(request.POST or None)

    if request.method == 'POST':
        if macrame_form.is_valid():
            macrame_form.save()
            return redirect('dash')

    context = {
        'macrame_form': macrame_form,
    }

    return render(request, 'add-macrame.html', context)


# def dashboard(request):
#     form = SearchForm(request.GET)
#     posts = Post.objects.all()
#
#     if request.method == "GET":
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             posts = posts.filter(title__icontains=query)
#
#     context = {
#         "posts": posts,
#         "form": form,
#     }
#
#     return render(request, 'posts/dashboard.html', context)

# def macrame(request):
#     return render(request, 'add-macrame.html')
#
#
# def macrame_view(request):
#     return render(request, 'add-macrame.html')