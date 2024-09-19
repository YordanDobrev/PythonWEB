from django.http import HttpResponse
from django.shortcuts import render

from Artonia.products.models import ArtPainting, Macrame


# Create your views here.

def index(request):
    art_paintings = request.GET.get('art_paintings', '')
    art_paintings = ArtPainting.objects.filter(name__icontains=art_paintings)

    macrame = request.GET.get('macrame', '')
    macrame = ArtPainting.objects.filter(name__icontains=macrame)

    context = {
        'art_paintings': art_paintings,
        'macrame': macrame,
    }

    return render(request, 'products.html', context)
