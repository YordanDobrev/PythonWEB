from django.shortcuts import render


# Create your views here.

def dashboard(request):
    render(request, 'post/dashboard.html')


def create_post(request):
    render(request, 'post/create-post.html')


def delete_post(request):
    render(request, 'post/delete-post.html')


def edit_post(request):
    render(request, 'post/edit-post.html')


def details_post(request):
    render(request, 'post/details-post.html')
