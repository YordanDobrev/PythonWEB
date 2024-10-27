from django.shortcuts import render


def author_creation(request):
    return render(request, 'author/create-author.html')


def author_details(request):
    return render(request, 'author/details-author.html')


def author_edit(request):
    return render(request, 'author/edit-author.html')


def author_delete(request):
    return render(request, 'author/delete-author.html')
